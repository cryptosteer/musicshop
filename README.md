### Music Shop

Cree una aplicacion web usando el framework django, que permita gestionar una tienda de musica.

Tenga en cuenta los siguientes modelos minimos a crear:

- Perfil
  - Vendedor
  - Cliente
- Tipo de articulo

		Ej: Cassete, LP, CD, VHS, DVD, Otros

- Articulo
  - Genero, Tipo, Album, Artista, Año, Valor
- Pedido
  - Cliente, Vendedor, Fecha, Total
- Detalle pedido
  - Articulo, Cantidad, Valor



Cree la configuracion del administrador para gestionar dichos modelos. Use formset para manejar la vista maestro / detalle del Pedido y el detalle del pedido.

Cree las urls, vistas, y plantillas segun requiera para realizar autenticacion, listar los articulos y crear los pedidos.

Se tendra en cuenta para la evaluacion final:

1. La totalidad de la aplicacion realizada (3/5)
2. Buenas practicas (1/5)
3. Interfaces visuales (Plantilla) bien diseñada (1/5)

# Usuarios de prueba

- username: jrnp97, password: 123456 - profile: seller
- username: lula, password: 123456 - profile: client

