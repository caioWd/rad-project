def init_controllers(app):
    @app.route("/")
    def init():
        return {"message":"hello, world"}