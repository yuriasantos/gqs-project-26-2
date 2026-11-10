class RepositorioUsuariosEmMemoria:
    def __init__(self):
        self._usuarios = {}

    def salvar(self, usuario):
        self._usuarios[usuario.email] = usuario

    def buscar_por_email(self, email):
        return self._usuarios.get(email)