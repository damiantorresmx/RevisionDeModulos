'''
Módulo: sh_rental_sales_validation/sale_order.py
Fecha: 2025-05-13
'''

from odoo import models, api, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    """
    Hereda sale.order.line para añadir validación de stock en la fase de cotización.

    Método:
        _onchange_qty_warning: Genera una advertencia al editar cantidad.
    """
    _inherit = 'sale.order.line'

    @api.onchange('product_uom_qty', 'product_id')
    def _onchange_qty_warning(self):
        """
        Al cambiar producto o cantidad en la línea de cotización:
        - Si el estado de la orden es 'draft' o 'sent', compara la cantidad solicitada
          con el stock disponible.
        - Si la solicitada supera la disponible, retorna un warning que se muestra al usuario.

        El warning permite guardar la cotización, pero recuerda que al confirmar la venta
        no podrás exeder el stock disponible.
        """
        if self.order_id.state in ('draft', 'sent') and self.product_id:
            available = self.product_id.qty_available
            requested = self.product_uom_qty
            if requested > available:
                return {
                    'warning': {
                        'title': _('Inventario insuficiente'),
                        'message': _(
                            'Advertencia: estás cotizando más unidades de las disponibles para %s.\n'
                            'Solicitado: %s  •  Disponible: %s\n\n'
                            'Podrás guardar la cotización, pero al confirmar la venta no podrás '
                            'superar el stock disponible.'
                        ) % (self.product_id.display_name, requested, available),
                    }
                }


class SaleOrder(models.Model):
    """
    Hereda sale.order para añadir validación estricta de stock al confirmar la venta.

    Métodos:
        action_confirm: Sobrescribe confirmación para validar stock en cada línea.
    """
    _inherit = 'sale.order'

    def action_confirm(self):
        """
        Antes de confirmar la venta, recorre cada línea de pedido y verifica:
        - Si la cantidad solicitada supera el stock disponible, lanza ValidationError
          indicando el máximo que hay en inventario.
        - Si todas las líneas cumplen, se delega al método estándar de confirmación.
        """
        for order in self:
            for line in order.order_line:
                if line.product_id:
                    available = line.product_id.qty_available
                    requested = line.product_uom_qty
                    if requested > available:
                        raise ValidationError(_(
                            'No puedes confirmar el pedido para %s con cantidad %s.\n'
                            'Sólo hay %s unidades disponibles en inventario.'
                        ) % (line.product_id.display_name, requested, available))
        return super(SaleOrder, self).action_confirm()
