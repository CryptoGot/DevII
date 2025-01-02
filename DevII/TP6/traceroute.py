import argparse
import subprocess
# argpase pour les options  et interface ligne commande et sobprocess pour le tracert
def lets_go(target, progressive, output_file):
    try:
        # list pour commande system et la cible
        command = ["tracert", target]

        if progressive:
            # pour la lecture progressive (lire au fur et a mesure)
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            file = None
            if output_file:
                file = open(output_file, 'w')  # pour ouvrire un fichier en write
            try:
                for line in iter(process.stdout.readline, ""):# pour lire chaque ligne des que possible
                    print(line.strip())  # pour afficher chaque saut
                    if file:
                        file.write(line)  # pour ecrire dans le fichier si il y a
            finally:
                if file:
                    file.close()  # pour fermer le fichier si ouvert
            process.stdout.close()
            process.wait()
        else:
            # pour afficher si pas de -p ou -o
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) #Attend que tout se termine avant d etre exec
            print(result.stdout)# pour afficher les résultat en terminal
            if output_file:
                with open(output_file, 'w') as file:
                    file.write(result.stdout)  # pour sauvegarder dans un fichier si spécifié
    except Exception as e: #en cas d erreur
        print(f"Erreur lors de l'exécution de traceroute : {e}")

def main():
    parser = argparse.ArgumentParser()# pour les arguments qu il accepte
    parser.add_argument("target")
    parser.add_argument("-p", "--progressive")
    parser.add_argument("-o", "--output-file")

    args = parser.parse_args() # pour analysser les argu pour qu il soit accesible via args
    lets_go(args.target, args.progressive, args.output_file)#appeler la methods

if __name__ == "__main__":
    main() # apeller main
