from receipt_tracker.flask import app, db

if __name__ == "__main__":
    # Start the flask application with development settings.

    app.run(debug=True)

    @app.teardown_appcontext
    def shudown_db_session(exeception=None):
        """Dispose of the current Session, if present.

        This will first call Session.close() method on the current Session, which releases any existing transactional/connection resources still being held; transactions specifically are rolled back. The Session is then discarded. Upon next usage within the same scope, the scoped_session will produce a new Session object.

        """
        db.remove()
