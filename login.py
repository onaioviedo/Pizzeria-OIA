import re
import sys

# Credenciales definidas por ti
CORREO_REGISTRADO = "admin@oiapizza.com"
CONTRASENA_REGISTRADA = "Clave*2026"

def validar_correo(correo):
    """Valida el formato del correo electrónico."""
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, correo) is not None

def validar_contrasena(contrasena):
    """
    Valida que la contraseña cumpla con:
    - Mínimo 8 caracteres
    - Al menos una letra minúscula
    - Al menos una letra mayúscula
    - Al menos un carácter especial
    """
    if len(contrasena) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    if not re.search(r'[a-z]', contrasena):
        return False, "La contraseña debe incluir al menos una letra minúscula."
    if not re.search(r'[A-Z]', contrasena):
        return False, "La contraseña debe incluir al menos una letra mayúscula."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        return False, "La contraseña debe incluir al menos un carácter especial."
    return True, "Contraseña válida."

def ejecutar_login():
    """Bucle de login que permite reintentar, salir con 'exit' y muestra guías de formato."""
    print("=== SISTEMA DE LOGIN ===")
    print("(Escribe 'exit' en cualquier momento para salir del programa)\n")
    
    while True:
        # 1. Pedir y validar el correo
        correo_ingresado = input("Ingresa tu correo electrónico (ej: usuario@oiapizza.com): ").strip()
        
        # Opción para salir del programa
        if correo_ingresado.lower() == 'exit':
            print("\nSaliendo del programa. ¡Hasta luego!")
            sys.exit()
            
        if not validar_correo(correo_ingresado):
            print("❌ [Error]: El formato del correo no es válido. Debe ser como: usuario@dominio.com\n")
            continue
        
        # 2. Mostrar guía de formato de contraseña
        print("💡 Formato de contraseña requerido:")
        print("   - Mínimo 8 caracteres")
        print("   - Al menos una letra minúscula y una mayúscula")
        print("   - Al menos un carácter especial (!@#$%^&*...)\n")
        
        contrasena_ingresada = input("Ingresa tu contraseña: ").strip()
        
        # Opción para salir del programa
        if contrasena_ingresada.lower() == 'exit':
            print("\nSaliendo del programa. ¡Hasta luego!")
            sys.exit()
            
        valida, mensaje = validar_contrasena(contrasena_ingresada)
        if not valida:
            print(f"❌ [Error]: {mensaje}\n")
            continue

        # 3. Verificar si coincide con el registrado
        if correo_ingresado == CORREO_REGISTRADO and contrasena_ingresada == CONTRASENA_REGISTRADA:
            print("\n✅ ¡Login exitoso! Bienvenido al sistema.")
            return True
        else:
            print("❌ [Error]: Correo o contraseña incorrectos. Inténtalo de nuevo.\n")