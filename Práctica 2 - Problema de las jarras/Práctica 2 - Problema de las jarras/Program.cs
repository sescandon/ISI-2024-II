
using Práctica_2___Problema_de_las_jarras;

Jar jar1 = new Jar(3);
Jar jar2 = new Jar(5);

while (true)
{
    Console.WriteLine("1. Llenar jarra 1");
    Console.WriteLine("2. Llenar jarra 2");
    Console.WriteLine("3. Vaciar jarra 1");
    Console.WriteLine("4. Vaciar jarra 2");
    Console.WriteLine("5. Llenar jarra 1 con jarra 2");
    Console.WriteLine("6. Llenar jarra 2 con jarra 1");
    Console.WriteLine("7. Salir \n");

    var option = Console.ReadLine();

    switch (option)
    {
        case "1":
            jar1.fill();
            break;
        case "2":
            jar2.fill();
            break;
        case "3":
            jar1.empty();
            break;
        case "4":
            jar2.empty();
            break;
        case "5":
            jar1.fill(jar2);
            break;
        case "6":
            jar2.fill(jar1);
            break;
        case "7":
            return;
        default:
            Console.WriteLine("Opción inválida");
            break;
    }

    Console.Clear();

    Console.WriteLine($"\nEl volumen de la jarra de {jar1.getCapacity()} litros es de {jar1.getCurrentVolume()}");
    Console.WriteLine($"El volumen de la jarra de {jar2.getCapacity()} litros es de {jar2.getCurrentVolume()}\n");

    if (jar1.getCurrentVolume() == 1 || jar2.getCurrentVolume() == 1)
    {
        Console.WriteLine("El reto fue completado");
        break;
    }

}

