from ldap3 import Server, Connection

server = Server('ldap://your-ldap-server.com')
conn = Connection(server, 'cn=admin,dc=example,dc=com', 'password')
conn.bind()

conn.search('dc=example,dc=com', '(objectClass=person)', attributes=['cn', 'mail'])
print(conn.entries)
