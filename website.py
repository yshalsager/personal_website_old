from personal_website import create_app, cli

app = create_app()
cli.register(app)

if __name__ == '__main__':
    app.run()
