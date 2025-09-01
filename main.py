from flask import Flask, render_template, request, jsonify

app_calculadora = Flask(__name__)

@app_calculadora.route("/")
def pagina_inicio():
    return render_template("index.html")

@app_calculadora.route("/binario")
def pagina_binario():
    return render_template("binario.html")

@app_calculadora.route("/hexadecimal")
def pagina_hexadecimal():
    return render_template("hexadecimal.html")

@app_calculadora.route("/octal")
def pagina_octal():
    return render_template("octal.html")

@app_calculadora.route("/convert", methods=["POST"])
def convertir_numero():
    try:
        datos_usuario = request.get_json()
        
        numero_decimal = int(datos_usuario.get('number', 0))
        tipo_conversion = datos_usuario.get('type')
        
        resultado = {
            'success': True,
            'decimal': numero_decimal
        }
        
        if tipo_conversion == 'binary':
            numero_binario = bin(numero_decimal)[2:]
            resultado['binary'] = numero_binario
            
        elif tipo_conversion == 'hexadecimal':
            numero_hex = hex(numero_decimal)[2:].upper()
            resultado['hexadecimal'] = numero_hex
            
        elif tipo_conversion == 'octal':
            numero_octal = oct(numero_decimal)[2:]
            resultado['octal'] = numero_octal
        
        return jsonify(resultado)
        
    except ValueError:
        error_respuesta = {
            'success': False,
            'error': 'Por favor ingrese un número válido'
        }
        return jsonify(error_respuesta)
        
    except Exception:
        error_general = {
            'success': False,
            'error': 'Error en la conversión'
        }
        return jsonify(error_general)

if __name__ == '__main__':
    app_calculadora.run(debug=True)