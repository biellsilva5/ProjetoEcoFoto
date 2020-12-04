# ProjetoEcoFoto
<br>
<strong> Documentação api EcoFoto</strong>
<br>
Rota : /administradores
<br>
GET<br>
Retorna uma lista de usuários/administradores cadastrados com o seguinte json(‘_id’, ‘name’ e ‘email’)
<br><br>
PUT<br>
Criação de um novo usuário/administrador, o servidor espera receber dados vindo de um form-data no corpo da request com os seguintes parâmetros (‘email’, ‘password’ e ‘name’), se o usuário for inserido, retorna uma resposta HTTP com status code 201
<br><br>
POST<br>
Atualização de dados de usuário/administrador, o servidor espera receber dados vindo de um form-data no corpo da request com os seguintes parâmetros(´_id´, ‘name’, ‘email’, ‘password’), se o usuário for atualizado, retorna uma resposta HTTP com status code 200
<br><br>
DELETE<br>
Apagar usuário/administrador, o servidor espera receber dados vindo de um form-data no corpo da request com o seguinte parâmetro(‘_id’), se o usuário for deletado, retorna uma resposta HTTP com status code 200 
<br><br>
Rota: /login<br>
POST<br>
Verificação de dados do usuário, o servidor espera receber os seguintes parâmetros(‘email’, ‘password’), se o email e senha conferir no banco de dados, retorna uma resposta HTTP com status code 200, caso contrário status code 401
<br><br>

Rota: /edicoes<br>
GET<br>
Retornar lista de edições cadastradas no sistema, com o seguinte json ('_id', 'name', 'assets', 'about', 'music', 'start_date', 'end_date', 'status')
<br><br>
PUT<br>
Criar uma edição no banco de dados,  o servidor espera receber dados vindo de um form-data no corpo da request com os seguintes parâmetros ('_id', 'name', 'assets', 'about', 'music', 'start_date', 'end_date', 'status')
<br><br>
POST<br>
Atualizar dados de um edição, o servidor espera receber dados vindo de um form-data no corpo da request com os seguintes parâmetros ('_id', 'name', 'assets', 'about', 'music', 'start_date', 'end_date', 'status')
<br><br>
DELETE<br>
Apagar edição, o servidor espera receber dados vindo de um form-data no corpo da request com o seguinte parâmetro(‘_id’), se a edição for deletar, retorna uma resposta HTTP com status code 200 
<br><br>
