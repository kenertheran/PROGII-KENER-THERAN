/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package vectores_java;

import java.util.ArrayList;
import java.util.Collections;


public class Vectores_Java {
    public static void main(String[] args) {
        ArrayList<Integer> lista = new ArrayList();
         System.out.println(lista);
    System.out.println("El tamaño de la lista es: " +lista.size());
    System.out.println(lista);
    
    
    ArrayList<String> vehiculos = new ArrayList();
        vehiculos.add("moto");
        vehiculos.add("carro");
        vehiculos.add("autobus");
        vehiculos.add("avion");
        vehiculos.add("helicoptero");
        System.out.println(vehiculos);    
     String primerElemento = vehiculos.get(0);
        System.out.println("Primer elemento: " + primerElemento);
        
        String centralElemento = vehiculos.get(2);
        System.out.println("Elemento central: " + centralElemento);
        
        String ultimoElemento = vehiculos.get(4);
        System.out.println("Ultimo elemento: " + ultimoElemento);
        
        ArrayList<String> datosPersonales = new ArrayList<>();

        datosPersonales.add("nombre: kener theran");
        datosPersonales.add("edad: 17 años"); 
        datosPersonales.add("estatura: 1.82"); 
        datosPersonales.add("estado civil: Soltero"); 
        datosPersonales.add("direccion: Zaragocilla sector el progreso Cra 50A"); 
        datosPersonales.add("ciudad: Cartagena");
        System.out.println(datosPersonales);
        
        
        ArrayList<String> it_companies = new ArrayList<>();
        it_companies.add("Facebook");
        it_companies.add("Google");
        it_companies.add("Microsoft");
        it_companies.add("Apple");
        it_companies.add("IBM");
        it_companies.add("Oracle");
        it_companies.add("Amazon");
        
        System.out.println("Lista de empresas de tecnologia:");
        System.out.println(it_companies);
        it_companies.add("Asus");
        System.out.println(it_companies);

        System.out.println("Lista de empresas de tecnologia:");
        System.out.println(it_companies);
        System.out.println("La empresa Amazon esta en la lista? " + it_companies .contains("Amazon")); 
        Collections.sort(it_companies);
        System.out.println("Ordenando la lista:  " +it_companies);
        Collections.reverse(it_companies);
        System.out.println("Lista de empresas de tecnologia en orden descendente:");
        System.out.println(it_companies);
        it_companies.remove(1);
        System.out.println("Imprimiendo Lista despues de eliminacion" +it_companies);
        it_companies.clear();
System.out.println("Imprimiendo Lista despues de vaciada" +it_companies);
        

        
      
    }
    
}
