# Operações com Sets no Python
grupos_hiphop = {'BTS','BigBang','BAP'}
grupos_pop = {'BTS','BlackPink','RedVelvet'}

# União
print("União - Todas os grupos (Únicas) ")
print(grupos_hiphop | grupos_pop)
print("==========================================================")

# Interseção
print("Interseção - Bandas em comum no rock alternativo e indie rock")
print(grupos_hiphop & grupos_pop)
print("==========================================================")

# Diferença
print("Diferença - Grupo que está no hiphop mas não está no pop")
print(grupos_hiphop - grupos_pop)
print("==========================================================")

# Diferença Simétrica
print("Diferença Simétrica - Grupos que estão apenas em hiphop ou apenas em pop")
print(grupos_hiphop ^grupos_pop)

#Adicionando um item no Sets no Python
grupos_hiphop.add('NCT')
print(grupos_hiphop)

#Remover um item do Set Python com remove()
bandas_rock_alternativo = {"Red Hot Chili Peppers", "Muse", "The Killers"}
bandas_rock_alternativo.remove("Muse") #Remove o item pelo próprio objeto
print(bandas_rock_alternativo) #{'Red Hot Chili Peppers', 'The Killers'}

#Remover um item do Set Python com discard()
bandas_rock_alternativo = {"Red Hot Chili Peppers", "Muse", "The Killers"}
bandas_rock_alternativo.discard("Muse") #Remove o item pelo próprio objeto
print(bandas_rock_alternativo) #{'Red Hot Chili Peppers', 'The Killers'}