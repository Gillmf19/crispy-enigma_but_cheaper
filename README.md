<p align="center">
  <h1>GEOGI – Similar to Geomike but different</h1>
  <p><em>Fueled by Geomike</em></p>
</p>

---

## Descripción

**GEOGI** es una aplicación web desarrollada con Django que permite realizar procesos de geocodificación a partir de direcciones ingresadas por el usuario, almacenando los resultados en una base de datos para su consulta posterior.

Esta versión corresponde a una edición personalizada del proyecto original — *GeoMike but cheaper* — concebida como una implementación académica con estructura de aplicación real, enfocada en demostrar arquitectura limpia, separación de responsabilidades y flujo completo de datos.

---

## Arquitectura

El sistema está construido bajo el patrón **MVT (Modelo–Vista–Template)**, lo que permite separar claramente:

- **Modelo** → Persistencia de datos en base de datos
- **Vista** → Lógica de negocio y procesamiento de solicitudes HTTP
- **Template** → Renderizado dinámico del frontend

Esta estructura garantiza organización, mantenibilidad y escalabilidad.

---

## Tecnologías Utilizadas

| Tecnología | Propósito |
|------------|------------|
| Django | Framework backend |
| Geopy | Geocodificación |
| SQLite | Base de datos |
| TailwindCSS (CDN) | Estilizado frontend |
| Font Awesome | Iconografía |

---

## Flujo del Sistema

1. El usuario ingresa una dirección.
2. El formulario envía una solicitud `POST`.
3. La vista procesa la dirección.
4. Se realiza la geocodificación.
5. Se almacenan latitud y longitud en la base de datos.
6. El historial actualizado se renderiza dinámicamente.

---

## Seguridad

El sistema incluye protección CSRF integrada en Django para evitar ataques de falsificación de solicitudes, asegurando que todas las operaciones `POST` estén validadas correctamente.

---

## Propósito Académico

Este proyecto no busca replicar un servicio comercial, sino demostrar:

- Integración completa frontend + backend  
- Uso correcto del ORM  
- Persistencia funcional en base de datos  
- Implementación estructurada bajo el patrón MVT  

---

<p align="center">
  <strong>GEOGI</strong><br>
  <em>Fueled by Geomike</em>
</p>
