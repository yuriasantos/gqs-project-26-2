from usuario import Usuario


class ServicoCadastro:
    def __init__(self, repositorio):
        self._repositorio = repositorio

    def cadastrar(self, nome, email, senha_hash):
        existente = self._repositorio.buscar_por_email(email)

        if existente is not None:
            raise ValueError("E-mail já cadastrado. Faça login.")

        usuario = Usuario(
            nome=nome,
            email=email,
            senha_hash=senha_hash,
        )

        self._repositorio.salvar(usuario)

        return usuario