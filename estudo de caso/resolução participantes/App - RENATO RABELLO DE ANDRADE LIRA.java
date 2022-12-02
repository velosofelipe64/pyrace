package org.example;

import org.eclipse.jgit.api.Git;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );

        int num = plusFive(10);

    }

    public static int plusFive(int num){

        return num + 5;
    }

}
