import sender_stand_request
import data
# esta función cambia los valores en el parámetro "name"
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función de prueba positiva
def positive_assert(name):
    # Crear un usuario primero
    user_response = sender_stand_request.post_new_user(data.user_body)

    # Obtener el token del usuario creado
    auth_token = user_response.json()["authToken"]

    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token )

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo name está en la respuesta y es el mismo
    assert kit_response.json()["name"] == name

# Prueba 1. Creación de un nuevo kit
# El parámetro "name" contiene un caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Prueba 2. Creación de un nuevo kit
# El parámetro "name" contiene 511 caracter
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabC")

# Función de prueba negativa
def negative_assert_symbol(name):
    # Crear un usuario primero
    user_response = sender_stand_request.post_new_user(data.user_body)

    # Obtener el token del usuario creado
    auth_token = user_response.json()["authToken"]

    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400

# Prueba 3. Creación de un nuevo kit
# El parámetro "name" contiene cero caracteres
def test_create_kit_0_letter_in_name_get_success_response():
    negative_assert_symbol("")

# Prueba 4. Creación de un nuevo kit
# El parámetro "name" contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert_symbol("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                           "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcd"
                           "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                           "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
# Prueba 5. Creación de un nuevo kit
# El parámetro "name" contiene caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\: ""№%@\",")

# Prueba 6. Creación de un nuevo kit
# El parámetro "name" contiene espacios
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7. Creación de un nuevo kit
# El parámetro "name" contiene string de numeros
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

# Función de prueba negativa
# El parametro name no se envia
def negative_assert_no_name(kit_body):
    # 1. Crear un usuario primero
    user_response = sender_stand_request.post_new_user(data.user_body)

    # 2. Obtener el token del usuario creado
    auth_token = user_response.json()["authToken"]

    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

# Prueba 8. Creación de un nuevo kit
# El parámetro "name" no se pasa en la solicitud
def test_create_kit_no_name_get_success_response():
    negative_assert_no_name("")

# Prueba 9. Error
# El tipo del parámetro "firstName" es un número
def test_create_kit_number_type_name_get_error_response():
    # 1. Crear un usuario primero
    user_response = sender_stand_request.post_new_user(data.user_body)

    # 2. Obtener el token del usuario creado
    auth_token = user_response.json()["authToken"]

    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit_body = get_kit_body(123)

    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400