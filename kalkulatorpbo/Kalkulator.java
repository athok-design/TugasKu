/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.kalkulatorpbo;

import java.util.Scanner;

public class Kalkulator {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        double angka1, angka2, hasil;
        char operator;

        System.out.print("Masukkan angka pertama: ");
        angka1 = input.nextDouble();

        System.out.print("Masukkan operator (+ - * /): ");
        operator = input.next().charAt(0);

        System.out.print("Masukkan angka kedua: ");
        angka2 = input.nextDouble();

        switch (operator) {

            case '+':
                hasil = angka1 + angka2;
                System.out.println("Hasil = " + hasil);
                break;

            case '-':
                hasil = angka1 - angka2;
                System.out.println("Hasil = " + hasil);
                break;

            case '*':
                hasil = angka1 * angka2;
                System.out.println("Hasil = " + hasil);
                break;

            case '/':
                if (angka2 != 0) {
                    hasil = angka1 / angka2;
                    System.out.println("Hasil = " + hasil);
                } else {
                    System.out.println("Tidak bisa dibagi dengan 0!");
                }
                break;

            default:
                System.out.println("Operator tidak tersedia!");
        }

        input.close();
    }
}