import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CBD.settings')
django.setup()

from mongoengine import connect
from mongoengine.errors import NotUniqueError
from users.models import MongoUser
from django.contrib.auth.hashers import make_password
from books.models import Book

def create_admin_user():
    print("Creating admin user...")
    connect('cbd')
    if not MongoUser.objects(is_admin=True).first():
        try:
            MongoUser(
                username='admin',
                password=make_password('4dm1n'),
                email='admin@admin.com',
                is_active=True,
                is_admin=True
            ).save()
            print("Admin user created.")
        except NotUniqueError:
            print("Admin user already exists.")
    else:
        print("An admin user already exists.")

def create_books():
    print("Creating books...")
    connect('cbd')
    if not Book.objects.first():    
        try:
            Book(isbn ='9788478884452',title='Harry Potter y la piedra filosofal',author='J.k. Rowling',year=1999,description='Harry Potter y la piedra filosofal es el primer volumen de la ya clásica serie de novelas fantásticas de la autora  británica J.K. Rowling.',genre='Aventuras',pages=264,language='Español',show=True, image_link='https://static.wikia.nocookie.net/esharrypotter/images/9/9a/Harry_Potter_y_la_Piedra_Filosofal_Portada_Espa%C3%B1ol.PNG/revision/latest/scale-to-width-down/1200?cb=20151020165725').save()
            Book(isbn ='9782409031564',title='Aprender la programación orientada a objetos con el lenguaje Python',author='Vincent Boucheny',year=2021,description='Este libro sobre el aprendizaje de la programación orientada a objetos con el lenguaje Python, se dirige a cualquier persona que desee dominar este tipo de programación. Conocimientos básicos de desarrollo y de la sintaxis del lenguaje Python, son requisitos previos esenciales para sacar el máximo partido al libro. ',genre='Educativo',pages=282,language='Español',show=True, image_link='https://imagessl4.casadellibro.com/a/l/s7/64/9782409031564.webp').save()
            Book(isbn ='9788491162506',title='Introducción a las bases de datos NoSQL usando MongoDB',author='Antonio Sarasa',year=2016,description='En este manual  lleva a cabo una introducción a las bases de datos NoSQL en el contexto de MongoDB, una base de datos NoSQL de tipo documental. El objetivo de la obra es acercar al lector a los conceptos y modelos que se gestionan en las bases de datos  NoSQL usando un producto concreto. Se ha elegido MongoDB al tratarse de una base de datos NoSQL, que en los últimos años se extendió con gran rapidez constituyendo una sólida alternativa a las bases de datos SQL convencionales. El primer capítulo de la obra tiene un objetivo introductorio y consiste en una revisión de los conceptos y definiciones fundamentales acerca de las bases de datos NoSQL. El resto de capítulos del libro se dedican a revisar las diferentes funcionalidades de MongoDB. Algunos capítulos van acompañados de una propuesta de ejercicios prácticos, cuyas soluciones pueden encontrarse al final del libro. ',genre='Educativo',pages=308,language='Español',show=True, image_link='https://imagessl6.casadellibro.com/a/l/s7/06/9788491162506.webp').save()
            Book(isbn ='9788411074278',title='La ciudad y sus muros inciertos',author='Haruki Murakami',year=2024,description='Poco se imagina el joven protagonista de esta novela que la chica de la que se ha enamorado está a punto de desaparecer de su vida. Se han conocido durante un concurso entre estudiantes de diferentes institutos, y no pueden verse muy a menudo. En sus encuentros, sentados bajo la glicinia de un parque o paseando a orillas de un río, la joven empieza a hablarle de una extraña ciudad amurallada, situada, al parecer, en otro mundo; poco a poco, ella acaba confesándole su inquietante sensación de que su verdadero yo se halla en esa misteriosa ciudad. De pronto, entrado el otoño, el protagonista recibe una carta de ella que quizá suponga una despedida, y eso lo sume en una profunda tristeza. Tendrán que pasar años antes de que pueda atisbar alguna posibilidad de reencontrarla. Y sin embargo, esa ciudad, tal y como ella la describió, existe. Porque todo es posible en este asombroso universo donde la realidad, la identidad, los sueños y las sombras fluctúan y escapan a los rígidos límites de la lógica.',genre='Ficción',pages=576,language='Español',show=True, image_link='https://imagessl8.casadellibro.com/a/l/s7/78/9788411074278.webp').save()
            Book(isbn ='9788411074124',title='La última función',author='Luis Landero',year=2024,description='Un grupo de amigos jubilados todavía recuerda la tarde de aquel domingo de enero de 1994 en que un Tito Gil maduro hizo su aparición en el bar restaurante del pueblo, en la Sierra de Madrid. Lo reconocieron por su prodigiosa voz. Regresaba a su lugar natal el afamado actor, el niño prodigio, la gran promesa teatral que parecía haber triunfado en los escenarios de la capital, o tal vez de medio mundo. Quizá en busca de notoriedad, Tito Gil no tardará en proponerles una gran representación colectiva con la que revitalizar el turismo y atraer a gente. Será la última oportunidad de evitar el despoblamiento paulatino. Nadie parece resistirse, pero necesitan a una gran actriz que le dé a él la réplica. En esas fechas, Paula, una mujer que ha visto aplastados sus sueños por la rutina laboral, toma el último tren en Atocha y despierta, sin saberlo, en la estación de un pueblo para ella desconocido. Bajo el sortilegio de un relato oral colectivo, en La última función Luis Landero vuelve a deleitarnos con la fascinación de una historia y de unos personajes que parecen salir de la bruma y tomar la escena para sentirse transformados. Una historia de amor inesperada, y un sinfín de personajes secundarios humorísticos y admirables que culminan en un magistral desenlace.',genre='Ficción',pages=224,language='Español',show=True, image_link='https://imagessl4.casadellibro.com/a/l/s7/24/9788411074124.webp').save()
            Book(isbn ='9780141033570',title='Thinking fast and slow',author='Daniel Kahneman',year=2012,description="Why is there more chance we'll believe something if it's in a bold type face? Why are judges more likely to deny parole before lunch? Why do we assume a good-looking person will be more competent? The answer lies in the two ways we make choices: fast, intuitive thinking, and slow, rational thinking. This book reveals how our minds are tripped up by error and prejudice (even when we think we are being logical), and gives you practical techniques for slower, smarter thinking. It will enable to you make better decisions at work, at home, and in everything you do.",genre='No ficción',pages=512,language='Inglés',show=True, image_link='https://imagessl0.casadellibro.com/a/l/s7/70/9780141033570.webp').save()
            Book(isbn ='9788408282501',title='El Rulas 2. El Rulas y la Copa Legendaria (Jóvenes influencers)',author='ANIMALIZE21',year=2024,description='EL RULAS, el personaje más macarra y divertido de ANIMALIZE21, quiere cumplir su sueño de ser futbolista en esta épica aventura a todo color. ¡PERO NECESITA TU AYUDA! Quiere demostrar a todo el mundo que es capaz de ganar LA COPA LEGENDARIA, el torneo de fútbol más épico de la ciudad.',genre='Aventuras',pages=144,language='Español',show=True, image_link='https://imagessl1.casadellibro.com/a/l/s7/01/9788408282501.webp').save()
            Book(isbn ='9788466671637',title='Anatomía del mal: 8 crímenes que te harán perder la fe en la humanidad (Somos B)',author='Jordi Wild',year=2024,description='En estas páginas nos embarcaremos en un viaje inquietante a través de ocho crímenes, cada cual más terrible, con los que os mostraré y reflexionaré sobre la maldad y cómo puede infiltrarse en los sitios menos esperados. Indagaré dentro de las mentes enfermas de asesinos, psicópatas, ególatras y monstruos, revelando, desde una perspectiva psicológica y científica, cuáles fueron sus motivaciones y más oscuros secretos que los llevaron a cometer estos crímenes imperdonables.',genre='Crimen',pages=304,language='Español',show=True, image_link='https://imagessl7.casadellibro.com/a/l/s7/37/9788466671637.webp').save()
            print("Books created.")
        except:
            print("A error ocurred.")
    else:
        print("Books already exists.")

if __name__ == '__main__':
    create_admin_user()
    create_books()