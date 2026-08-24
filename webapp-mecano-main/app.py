import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

'''@app.route("/mecano")
def mecano():
    return render_template("mecano.html")

@app.route("/hadas")
def hadas():
    return render_template("hadas.html")

@app.route("/sol")
def sol():
    return render_template("sol.html")

@app.route("/suelo")
def suelo():
    return render_template("suelo.html")
'''

@app.route("/album/<int:id>")
def album(id):
    match id:
        case 1:
            return render_template("detalle_album.html",
                                nombre="Mecano (1981)",
                                imgnum="1",
                                albumid="2n1N39ZjNXxzoyDkYm6yid",
                                descripcion="Mecano es el primer álbum de estudio debut de la banda, lanzado el 5 de abril " \
                                "de 1982 a través de Columbia Records. Es conocido popularmente como el álbum El Reloj, por " \
                                "su diseño de la portada. Despliega un tecno-pop muy incipiente, estilo que, sin dejar a un " \
                                "lado la originalidad de sus letras, el grupo irá depurando a lo largo de su carrera hasta " \
                                "hacerlo mucho más internacional, comercial y accesible a todo tipo de público.")
        case 2:
            return render_template("detalle_album.html",
                                nombre = "¿Dónde está el país de las hadas?",
                                imgnum="2",
                                albumid="395Ts8cMrWtmDHxrlYcTxz",
                                descripcion="¿Dónde está el país de las hadas? es el segundo álbum de estudio de la " \
                                "banda , publicado el 30 de mayo de 1983 por Columbia Records. El título del álbum, " \
                                "que vendió en España 100 000 copias, está tomado del tema instrumental homónimo que " \
                                "abre el trabajo, compuesto por Nacho Cano. El disco contó con la producción de " \
                                "Jorge Álvarez y del propio grupo y los arreglos de Luis Cobos, que también se encargó " \
                                "de arreglar y dirigir la sección de cuerdas del tema instrumental que da título al " \
                                "álbum, grabada en el Estudio 1 de la CBS en Londres, hecho que sería frecuente a " \
                                "partir de entonces por parte del grupo, ya en su etapa de madurez.")
        case 3:
            return render_template("detalle_album.html",
                                nombre = "Ya viene el sol",
                                imgnum="3",
                                albumid="1m3nnPAQcMKR86QDfWsguj",
                                descripcion="Ya viene el Sol es el tercer álbum de estudio de la banda, lanzado el 16 " \
                                "de octubre de 1984 a través de Columbia Records. Es un disco que se diferencia " \
                                "notablemente de sus dos trabajos anteriores, ya que introduce sonidos más novedosos, " \
                                "como el sampler/workstation Fairlight. Además, a partir de este trabajo el grupo " \
                                "asumió la producción de sus restantes álbumes. Es el primer disco en el que no se " \
                                "incluye un tema instrumental, como sí ocurría en los dos anteriores, y en él aparece " \
                                "la única canción en cuya composición participa Ana Torroja, aportando parte de la letra " \
                                "del tema Mosquito.")

        case 4:
            return render_template("detalle_album.html",
                                nombre = "Entre el cielo y el suelo",
                                imgnum="4",
                                albumid="1vDYLED9bQwm3FzIdXs5H9",
                                descripcion="Entre el Cielo y el Suelo es el cuarto álbum de estudio de la banda de " \
                                "tecno-pop Mecano, publicado el 21 de junio de 1986 a través de Sony BMG. Después de " \
                                "su ruptura con CBS, marcó un antes y un después en la trayectoria de la banda, " \
                                "iniciando con él una etapa de madurez creativa, conceptual y técnica que supondría su " \
                                "salto al éxito internacional. El álbum reivindicó la figura de José María Cano como " \
                                "compositor frente a su hermano Nacho, ya que previamente casi todos los temas del " \
                                "grupo que habían sido publicados como singles habían sido escritos por este último. " \
                                "El disco toma su nombre del primer verso de una de las canciones que aparecían en él, " \
                                "Me cuesta tanto olvidarte. Este álbum vendió más de 1 000 000 de ejemplares solamente " \
                                "en España. Este fue el primer álbum con el que superaron el millón de discos vendidos.")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
