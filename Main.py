import argparse, datetime, Simulacion

def main():
	parser = argparse.ArgumentParser("TC2008B RETO", description = "Base del reto");
	subparsers = parser.add_subparsers();

	subparser = subparsers.add_parser("RETO",  description = "Corre simulacion");
	subparser.add_argument("--CSV", required = True, type = str, help = "Archivo CSV de entrada");
	subparser.add_argument("--vRackC", required = True, type = str, help = "Dimensiones del rack de congelados en formato largo,ancho,alto,separaciones (centimetros)");			
	subparser.add_argument("--vRackR", required = True, type = str, help = "Dimensiones del rack de congelados en formato largo,ancho,alto,separaciones (centimetros)");			
	subparser.add_argument("--vRackS", required = True, type = str, help = "Dimensiones del rack de congelados en formato largo,ancho,alto,separaciones (centimetros)");			
	subparser.add_argument("--confianza", required = False, type = int, default=10, help = "Porcentaje de confianza");
	subparser.add_argument("--salida", required = False, type = str, default="salida.csv", help = "Nombre del archivo de salida");			

 


	subparser.set_defaults(func = Simulacion.Simulacion);

	Options = parser.parse_args();

	print(str(Options) + "\n");

	Options.func(Options);


if __name__ == "__main__":
	print("\n" + "\033[0;32m" + "[start] " + str(datetime.datetime.now()) + "\033[0m" + "\n");
	main();
	print("\n" + "\033[0;32m" + "[end] "+ str(datetime.datetime.now()) + "\033[0m" + "\n");



