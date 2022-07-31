import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('All about Python',
             'Python is a popular programming language. It is used for: web development (server-side), software '
             'development, mathematics, system scripting, and many other purposes. Python is a programming language '
             'developed by Guido van Rossum from the Netherlands, in 1990. It is considered a multi-purpose '
             'programming language since software developers can create code for any programming task. It is an '
             'interpreted programming language which means that an interpreter translates and executes one statement '
             'at a time. Python is used for many purposes including web development, scientific and numeric uses and '
             'education. Python is an excellent programming language for teaching programming, both at the '
             'introductory level and in more advanced courses. Recently, Python has been used to develop some code to '
             'demonstrate the effect of a virus in our organs.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Data Science Applications: Targeted Advertisements on Instagram',
             'Game analytics and movie analytics are not the only data science applications. Targeted advertisements '
             'are also useful tools. Instagram has targeted advertisements as an options in the “Ad Manager” section. '
             'There you can create a campaign to reach a specific audience and sell a product. This tool also allows '
             'you to modify and monitor the campaign whenever you want. One of the best features of Instagram Ads is '
             'that it allows you to classify the audience. Thus, the people who see your ad are more interested in '
             'your message than the general public. Instagram Ads uses artificial intelligence, machine learning, '
             'and algorithms. These data science tools help you reach a better-defined audience and keep to a set '
             'budget. They also help you achieve greater brand exposure, increased traffic, and higher engagement.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Big Data Applications',
             'Big data applications has increased the demand for data scientists who are specialists in managing and '
             'analyzing data. Developed economies are increasingly using the internet and networked mobile devices '
             'and this has intensified the volume of data that is being generated. Some estimates show that a third '
             'of the information stored in big data technologies is made up of images and alphanumeric text. We live '
             'in a world with massive competition to collect data. Often, companies develop project with big data to '
             'achieve certain objectives, such as improving customer experience, reducing costs, and marketing. Cloud '
             'computing has become an excellent tool to do this because it facilitates the development of big data '
             'projects for other industries. Governments, banking industries, insurance companies, and e-commerce '
             'sectors are cloud computing services and hire data scientists to develop their business ideas. '
             'Recently, data breaches have become a worrying problems for the different sectors that generate and '
             'manage large data warehouses. Because of this, big data technologies face the challenge of '
             'incorporating improved data security for different sectors.')
            )
connection.commit()
connection.close()

