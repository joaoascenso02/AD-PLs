from requests_oauthlib import OAuth2Session
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# credenciais da app cliente registada no github
client_id = "1c41d0a9c0d1e42a4046"
client_secret = "8dab435fe66c49fa07ca612d39af05d733a76d91"

# URIs do github para obtencao
# do authorization_code, do token, de callback e do recurso protegido
authorization_base_url = "https://github.com/login/oauth/authorize"
token_url = "https://github.com/login/oauth/access_token"
redirect_uri = "http://localhost"
protected_resource = "https://api.github.com/user"

github = OAuth2Session(client_id, redirect_uri=redirect_uri)

# pedido do authorization_code ao servidor de autenticacao (e do recurso a ceder)
authorization_url, state = github.authorization_url(authorization_base_url)
print(f"Aceder ao link para obter a autorizacao {authorization_url}")

# obter o authorization_code do servidor vindo no URL de redirecionamento
url_response = input("Insira o URL devolvido pelo browser aqui: ")

# obtencao do token
github.fetch_token(token_url, client_secret=client_secret,
                   authorization_response=url_response)

# acesso a um recurso protegido
r = github.get(protected_resource)
print(r.content.decode())
