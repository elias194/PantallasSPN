# CaPaz S.A. — Pantallas del sistema

Prototipo navegable con acceso de usuario y administrador, conservando la estructura de formularios, operaciones laterales y botones inferiores.

## Cómo usar esta actualización

1. Copiá `index.html`, `app.js` y `styles.css` a la carpeta del repositorio, reemplazando los archivos anteriores. Conservá los archivos de Git que ya están allí.
2. Abrí `index.html` con Edge o Chrome. También funciona como página estática en GitHub Pages.
3. Elegí la pestaña **Usuario** o **Administrador** al ingresar.

`index.html` incluye todo el CSS y JavaScript: también podés reemplazar solamente ese archivo para probar la actualización. Los archivos separados se entregan para facilitar la edición. Si editás `app.js` o `styles.css`, ejecutá `python construir.py` para actualizar el HTML antes de subirlo a GitHub Pages.

## Cuentas de demostración

| Tipo de acceso | Usuario o correo | Contraseña |
| --- | --- | --- |
| Administrador | `admin` | `capaz123` |
| Usuario | `valeria` o `valeria@example.com` | `capaz123` |
| Usuario | `nicolas` o `nicolas@example.com` | `capaz123` |
| Usuario | `camila` o `camila@example.com` | `capaz123` |

También se puede crear una cuenta desde **Usuario → Registrarme**. La contraseña elegida debe tener al menos 6 caracteres y coincidir con la confirmación. Las cuentas nuevas siempre son de usuario.

## Qué ve cada persona

- **Administrador:** los módulos anteriores de clientes, socios, cuotas, eventos, funciones, boletería, ventas web, tickets, informes y datos maestros. Desde Recursos humanos registra los actores y desde Eventos asigna el elenco.
- **Usuario:** Cartelera, Mis reservas, Mi membresía y Mi perfil. En Cartelera elige una función y reserva; Mis reservas muestra directamente todas sus reservas y entradas, incluidas las compras confirmadas en boletería. No puede gestionar registros de otras personas, modificar descuentos ni abrir módulos administrativos mediante el enlace interno.

Las pantallas de usuario muestran nombres de personas, documentos, obras, fechas y salas en lugar de los identificadores internos de cliente, venta, función o adhesión. Se conserva el número de entrada para reconocer cada ticket. Los identificadores internos siguen disponibles para el administrador.

Las compras web realizadas por el administrador requieren elegir el cliente. Las reservas de un usuario utilizan su propia identidad. El valor de descuentos para usuarios no puede alterarse desde la reserva; su gestión queda a cargo de Administración.

## Mi membresía

La vista de usuario presenta un resumen personal, sin formularios administrativos, identificadores, la pregunta “¿Es socio?” ni botones Guardar/Cancelar. El enlace existente `#misocio` continúa funcionando.

- Si está vigente y sin deuda: **Tu membresía está al día**, con la vigencia, saldo y último pago.
- Si hay deuda: **Tenés cuotas pendientes**, con el importe y una explicación adicional si también venció la membresía.
- Si venció y no hay deuda: orienta a renovar la membresía.
- Si está dada de baja: muestra **Inactiva** y explica cómo consultar su reactivación.
- Si comienza en una fecha futura: muestra **Próximamente**.
- Si no existe una adhesión: invita a consultar a Administración para asociarse y permite explorar la cartelera.

El historial muestra únicamente los pagos de cuotas de la persona que inició sesión. En celular los pagos se presentan como tarjetas para facilitar la lectura. Esta vista es informativa: las cuotas, altas y renovaciones se siguen gestionando desde Administración. La consulta administrativa conserva “¿Es socio?”, documentos, identificadores y demás datos de gestión.

## Cartelera y Mis reservas

El menú de usuario tiene una sola opción de **Cartelera**. En cada función, **Reservar entradas** despliega el campo de cantidad y el importe total dentro de la misma tarjeta. Al confirmar, se abre **Mis reservas** con la nueva reserva.

**Mis reservas** muestra una sola tarjeta por función: misma obra, fecha, hora y sala. Si se reservaron o compraron entradas en varias operaciones, se reúnen en esa tarjeta y se suman por separado las pagadas, pendientes y canceladas. La misma obra en otra fecha, horario o sala conserva su propia tarjeta. Las operaciones y los números de entrada originales no se modifican al agrupar.

**Ver entradas** despliega las entradas vigentes de la función. Las anuladas aparecen en **Ver entradas canceladas**, dentro de la misma tarjeta. Si todavía no hay reservas, se muestra un enlace a la cartelera.

- Las nuevas reservas quedan en estado **Reservada / Pendiente de pago** y ocupan los lugares solicitados. No se contabilizan como ventas cobradas en los informes.
- El usuario puede **Cancelar pendientes** antes del comienzo de la función. La confirmación indica la obra y la cantidad de entradas pendientes; Volver o Escape no modifican las reservas.
- Cancelar afecta solo a las entradas pendientes de esa función: se anulan, se libera el cupo correspondiente y se conserva el historial dentro de la misma tarjeta. Las entradas pagadas se mantienen. No se borran tickets ni operaciones.
- Solo se pueden cancelar reservas propias pendientes. Las compras **Confirmadas** de versiones anteriores se conservan como compras confirmadas y requieren consultar a Administración para una eventual cancelación.
- En el prototipo, Administración puede pasar una reserva a **Confirmada** desde **Venta vía web → Modificar estado**. Este cambio no realiza un cobro externo. Los informes cuentan las operaciones confirmadas.
- Los enlaces antiguos de usuario a `#web` y `#tickets` redirigen a Cartelera y Mis reservas respectivamente. Los módulos administrativos conservan sus operaciones.

## Pago desde el acceso de usuario

1. En **Mis reservas**, pulsá **Pagar pendientes** en la función correspondiente.
2. Revisá la cantidad y el importe: se incluyen únicamente las entradas pendientes de pago de esa función.
3. Elegí **Tarjeta** o **Transferencia** y pulsá **Confirmar pago simulado**. No se piden datos bancarios ni se realiza un cargo real.

Las operaciones incluidas pasan a **Confirmada**, las entradas figuran como pagadas y el importe pendiente queda en cero. La función sigue en una sola tarjeta, sin volver a consumir lugares ni generar tickets nuevos. Se guarda el medio, la fecha y una referencia de demostración para cada operación incluida. El informe de ventas usa la fecha de pago de estas operaciones, conservando la fecha de reserva.

No se pueden pagar reservas ajenas, anuladas, ya pagadas o de funciones no disponibles. El importe se calcula a partir de los registros guardados. Antes de confirmar se vuelven a comprobar estados, función e importe; un cambio invalida el pago completo, sin confirmar solo una parte. Volver o Escape cierran el resumen sin modificar los registros.

## Registro y validaciones

- Usuario o contraseña incorrectos: muestra un mensaje de error.
- Usuario, correo o documento ya registrados: rechaza el alta sin duplicar registros.
- El usuario y el correo se comparan sin distinguir mayúsculas y minúsculas.
- Campos vacíos, correo inválido, DNI incorrecto, contraseña corta y confirmación diferente: muestra un error en el formulario.
- Cantidades, cupos, fechas, edad mínima, referencias en uso y duplicados de cliente conservan sus validaciones.
- Al cerrar sesión se vuelve al acceso. La sesión se conserva al recargar en la misma pestaña.

## Varios actores en una obra

1. En **Recursos humanos**, registrá a cada persona con un rol cuyo nombre identifique a un **Actor / Actriz** (el rol y tres actores de ejemplo ya están cargados).
2. En **Eventos**, elegí el tipo **Teatro** y marcá a las personas en **Elenco de la obra**. Se pueden seleccionar varias, sin un máximo fijo.
3. El elenco queda guardado al registrar o modificar el evento, se muestra al consultarlo y aparece en la cartelera.

Se exige al menos un actor para un evento de teatro; se admiten dos, tres o más. No se puede eliminar una persona mientras integre el elenco de una obra. Para eventos de cine o música no se exige este campo.

## Datos anteriores y alcance

Los datos se guardan únicamente en el almacenamiento local de ese navegador. La actualización conserva los datos anteriores de CaPaz y agrega cuentas y elencos mediante una migración. Los clientes preexistentes reciben acceso inicial con su correo y la contraseña de demostración `capaz123`; sus nuevas cuentas usan como usuario la parte anterior a `@` (con un sufijo si hay coincidencias). Las cuentas creadas después utilizan la contraseña elegida en el registro.

Si abrís otra copia en una ubicación distinta, otro navegador o la versión de GitHub Pages, podés ver un almacenamiento diferente. No se sincronizan registros entre equipos. Al borrar los datos del navegador se pierden las altas guardadas allí.

Sigue siendo un prototipo académico sin servidor: la separación de roles funciona en la interfaz y las contraseñas de los usuarios se almacenan como un derivado PBKDF2 con sal, pero no constituye autenticación de producción. Los archivos y datos locales son accesibles desde las herramientas del navegador. Los pagos, correos y tickets no realizan operaciones externas.

## Comprobaciones de esta versión

Se verificaron en Chromium el registro y acceso, la separación por rol, el control de cupo, la persistencia, los formularios administrativos, los elencos y los informes. Se probaron la agrupación de operaciones de una misma función, la separación de funciones distintas, los totales mixtos de entradas pagadas y pendientes, el pago de varias reservas en una sola confirmación, la prevención de pagos duplicados, el registro por fecha de pago, la cancelación solo de pendientes y la conservación de los tickets originales. También se comprobaron los errores de importe o estado cambiado, la privacidad entre usuarios y el diseño a 1440 y 390 píxeles.
