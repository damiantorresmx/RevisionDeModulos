{
    'name': 'Validación de Ventas de Alquiler Personalizada',
    'version': '18.0',
    'summary': 'Añade validación de inventario para ventas de alquiler al crear cotizaciones/pedidos de venta.',
    'category': 'Sales',
    'depends': ['sale', 'stock'],  # Dependencias necesarias: 'sale' y 'stock' 
    'data': [
        # No necesitamos archivos de vista al principio, solo lógica de modelo
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}