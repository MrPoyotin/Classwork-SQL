import java.sql.*;
import java.util.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.Reader;
import java.sql.Connection;
import java.sql.DriverManager;
import org.apache.ibatis.jdbc.ScriptRunner;

public class Student{
    static Connection con;
    static Statement stmt;

    public static void main(String argv[])
    {
	connectToDatabase();
    }

    @SuppressWarnings("resource")
    public static void connectToDatabase()
    {

	String driverPrefixURL="jdbc:oracle:thin:@";
	String jdbc_url="artemis.vsnet.gmu.edu:1521/vse18c.vsnet.gmu.edu";
	
        // IMPORTANT: DO NOT PUT YOUR LOGIN INFORMATION HERE. INSTEAD, PROMPT USER FOR HIS/HER LOGIN/PASSWD
        System.out.print("Please enter your username for using JDBC\n");
        Scanner scan = new Scanner(System.in);
        String s = scan.next();

        System.out.print("Please enter your password associated with that username\n");
        Scanner scan2 = new Scanner(System.in);
        String s2 = scan.next();
   

        String username=s;
        String password=s2;
	
        try{
	    //Register Oracle driver
            DriverManager.registerDriver(new oracle.jdbc.driver.OracleDriver());
        } catch (Exception e) {
            System.out.println("Failed to load JDBC/ODBC driver.");
            return;
        }

       try{
            System.out.println(driverPrefixURL+jdbc_url);
            con=DriverManager.getConnection(driverPrefixURL+jdbc_url, username, password);
            DatabaseMetaData dbmd=con.getMetaData();
            stmt=con.createStatement();

            System.out.println("Connected.");

            if(dbmd==null){
                System.out.println("No database meta data");
            }
            else {
                System.out.println("Database Product Name: "+dbmd.getDatabaseProductName());
                System.out.println("Database Product Version: "+dbmd.getDatabaseProductVersion());
                System.out.println("Database Driver Name: "+dbmd.getDriverName());
                System.out.println("Database Driver Version: "+dbmd.getDriverVersion());
            }
            ScriptRunner sr = new ScriptRunner (con);
            System.out.print("Please enter the location of the paper.sql file.\n");
            Scanner scan7 = new Scanner(System.in);
            String s7 = scan7.nextLine();
            String location = s7 + "\\paper.sql";
            Reader reader = new BufferedReader(new FileReader(location));
            sr.runScript(reader);

            /*String sqlQuery = "SELECT Title FROM Publications WHERE PublicationID > 80";
            PreparedStatement pstmt = con.prepareStatement(sqlQuery);
            ResultSet rset = pstmt.executeQuery();
            while(rset.next()){
                //System.out.println(rset.getString(1));
            }*/
            int choice = 1;
            while(choice != 4){
            System.out.println("Please choose between these 4 options:");
            System.out.println("Option 1 - View Table Contents");
            System.out.println("Option 2 - Search by PUBLICATION ID");
            System.out.println("Option 3 - Search by one or more attributes");
            System.out.println("Option 4 - Exit");
            System.out.println("Select an option by typing in the desired option number.");
            Scanner scan3 = new Scanner(System.in);
            int s3 = scan3.nextInt();
            choice = s3;
            if(choice == 1){
                int bothOptions = 2;
                int noInvalids = 0;
                int firstY = 0;
                int secondY = 0;
                while(bothOptions == 2 || noInvalids > 0){
                    noInvalids = 0;
                    bothOptions = 0;
                    firstY = 0;
                    secondY = 0;
                    System.out.println("Would you like to see PUBLICATIONS?");
                    System.out.println("Please enter Y/N:");
                    Scanner scan4 = new Scanner(System.in);
                    String s4 = scan4.next();
                    if(s4.equals("Y") || s4.equals("y")){
                        firstY += 1;
                    }
                    else if(s4.equals("N") || s4.equals("n")){
                        bothOptions += 1;
                    }
                    else{
                        noInvalids += 1;
                    }
                    System.out.println("Would you like to see AUTHORS?");
                    System.out.println("Please enter Y/N:");
                    Scanner scan5 = new Scanner(System.in);
                    String s5 = scan5.next();
                    if(s5.equals("Y") || s5.equals("y")){
                        secondY += 1;
                    }
                    else if(s5.equals("N") || s5.equals("n")){
                        bothOptions += 1;
                    }
                    else{
                        noInvalids += 1;
                    }
                    if(bothOptions == 2){
                        System.out.println("Please choose Y for one or more of the two options.");
                    }
                    else if(noInvalids > 0){
                        System.out.println("You have entered an invalid answer for one or more of the two prompts.");
                    }
                    else{
                        if(firstY == 1 && secondY == 0){
                            System.out.println("Now displaying contens of the PUBLICATIONS table:\n");
                            String sqlQuery = "SELECT * FROM Publications";
                            PreparedStatement pstmt = con.prepareStatement(sqlQuery);
                            ResultSet rset = pstmt.executeQuery();
                            while(rset.next()){
                                System.out.println(rset.getInt(1) + ", " + rset.getInt(2) + ", " + rset.getString(3) + ", " + rset.getString(4)+ ", " + rset.getString(5) + "\n");
                            }
                        }
                        else if(firstY == 0 && secondY == 1){
                            System.out.println("Now displaying contens of the AUTHORS table:\n");
                            String sqlQuery = "SELECT * FROM Authors";
                            PreparedStatement pstmt = con.prepareStatement(sqlQuery);
                            ResultSet rset = pstmt.executeQuery();
                            while(rset.next()){
                                System.out.println(rset.getInt(1) + ", " + rset.getString(2) + "\n");
                            }
                        }
                        else{
                            System.out.println("Now displaying contens of the PUBLICATIONS table:\n");
                            String sqlQuery = "SELECT * FROM Publications";
                            PreparedStatement pstmt = con.prepareStatement(sqlQuery);
                            ResultSet rset = pstmt.executeQuery();
                            while(rset.next()){
                                System.out.println(rset.getInt(1) + ", " + rset.getInt(2) + ", " + rset.getString(3) + ", " + rset.getString(4)+ ", " + rset.getString(5) + "\n");
                            }
                            System.out.println("Now displaying contents of the AUTHORS table:\n");
                            String sqlQuery2 = "SELECT * FROM Authors";
                            PreparedStatement pstmt2 = con.prepareStatement(sqlQuery2);
                            ResultSet rset2 = pstmt2.executeQuery();
                            while(rset2.next()){
                                System.out.println(rset2.getInt(1) + ", " + rset2.getString(2) + "\n");
                            }
                        }
                    }
                }
            }
            if(choice == 2){
                int invalid = 1;
                while(invalid == 1){
                invalid = 0;
                System.out.println("Please enter a valid publication ID:");
                Scanner scan6 = new Scanner(System.in);
                int s6 = scan6.nextInt();
                if(s6 <= 0 || s6 > 91){
                    System.out.println("That was an invalid publication ID!");
                    invalid += 1;
                }
                else{
                    String sqlQuery = "SELECT Year, Type, Title, Summary FROM Publications WHERE PublicationID = " + s6;
                            PreparedStatement pstmt = con.prepareStatement(sqlQuery);
                            ResultSet rset = pstmt.executeQuery();
                            while(rset.next()){
                                System.out.print(rset.getInt(1) + ", " + rset.getString(2) + ", " + rset.getString(3)+ ", " + rset.getString(4));
                            }
                    String sqlQuery2 = "SELECT Author FROM Authors WHERE PublicationID = " + s6;
                            PreparedStatement pstmt2 = con.prepareStatement(sqlQuery2);
                            ResultSet rset2 = pstmt2.executeQuery();
                            int i = 0;
                            while(rset2.next()){
                                i += 1;
                                System.out.print(", ");
                                System.out.print(rset2.getString(1));
                            }
                            System.out.print("\n");
                            System.out.print("In this paper there are ");
                            System.out.print(i);
                            System.out.println(" authors.");
                }
            }
            }
            while(choice == 3){
                System.out.println("Please enter the input fields.");
                System.out.println("To skip a field please type in 'N' or 'n'");
                int yesCheck = 0;
                int fYCheck = 0;
                System.out.println("Author:");
                Scanner authorScan = new Scanner(System.in);
                String aS = authorScan.nextLine();
                if(!(aS.equals("N") || aS.equals("n"))){
                    yesCheck += 1;
                }

                System.out.println("Title:");
                Scanner titleScan = new Scanner(System.in);
                String tiS = titleScan.next();
                if(!(tiS.equals("N") || tiS.equals("n"))){
                    yesCheck += 1;
                }

                System.out.println("Year:");
                Scanner yearScan = new Scanner(System.in);
                String yS = yearScan.next();
                if(!(yS.equals("N") || yS.equals("n"))){
                    yesCheck += 1;
                }

                System.out.println("Type:");
                Scanner typeScan = new Scanner(System.in);
                String tyS = typeScan.next();
                if(!(tyS.equals("N") || tyS.equals("n"))){
                    yesCheck += 1;
                }
                fYCheck = yesCheck;


                System.out.println("Please enter the output fields with Y or N.");
                System.out.println("PublicationID:");
                int secYesCheck = 0;
                int f2YCheck = 0;
                Scanner pubIDScan = new Scanner(System.in);
                String pidYNS = pubIDScan.next();
                if(pidYNS.equals("Y") || pidYNS.equals("y")){
                    secYesCheck += 1;
                }

                System.out.println("Author:");
                Scanner authorYNScan = new Scanner(System.in);
                String aYNS = authorYNScan.next();
                if(aYNS.equals("Y") || aYNS.equals("y")){
                    secYesCheck += 1;
                }

                System.out.println("Title");
                Scanner titleYNScan = new Scanner(System.in);
                String tiYNS = titleYNScan.nextLine();
                if(tiYNS.equals("Y") || tiYNS.equals("y")){
                    secYesCheck += 1;
                }

                System.out.println("Year:");
                Scanner yearYNScan = new Scanner(System.in);
                String yYNS = yearYNScan.next();
                if(yYNS.equals("Y") || yYNS.equals("y")){
                    secYesCheck += 1;
                }

                System.out.println("Type:");
                Scanner typeYNScan = new Scanner(System.in);
                String tyYNS = typeYNScan.next();
                if(tyYNS.equals("Y") || tyYNS.equals("y")){
                    secYesCheck += 1;
                }

                System.out.println("Summary:");
                Scanner summaryScan = new Scanner(System.in);
                String sYNS = summaryScan.nextLine();
                if(sYNS.equals("Y") || sYNS.equals("y")){
                    secYesCheck += 1;
                }
                f2YCheck = secYesCheck;



                System.out.println("Please enter a field to sort by. Or type N for no sorting.");
                System.out.println("Sorted By:");
                Scanner sortScan = new Scanner(System.in);
                String sorty = sortScan.next();


                String sqlQuery = "SELECT UNIQUE ";
                if(pidYNS.equals("Y") || pidYNS.equals("y")){
                    sqlQuery = sqlQuery + "Publications.PublicationID";
                    if((secYesCheck - 1) != 0){
                        sqlQuery = sqlQuery + ", ";
                        secYesCheck -= 1;
                    }
                    else{
                        sqlQuery = sqlQuery + " ";
                    }
                }
                if(aYNS.equals("Y") || aYNS.equals("y")){
                    sqlQuery = sqlQuery + "Authors.Author";
                    if((secYesCheck - 1) != 0){
                        sqlQuery = sqlQuery + ", ";
                        secYesCheck -= 1;
                    }
                    else{
                        sqlQuery = sqlQuery + " ";
                    }
                }
                if(tiYNS.equals("Y") || tiYNS.equals("y")){
                    sqlQuery = sqlQuery + "Title";
                    if((secYesCheck - 1) != 0){
                        sqlQuery = sqlQuery + ", ";
                        secYesCheck -= 1;
                    }
                    else{
                        sqlQuery = sqlQuery + " ";
                    }
                }
                if(yYNS.equals("Y") || yYNS.equals("y")){
                    sqlQuery = sqlQuery + "Year";
                    if((secYesCheck - 1) != 0){
                        sqlQuery = sqlQuery + ", ";
                        secYesCheck -= 1;
                    }
                    else{
                        sqlQuery = sqlQuery + " ";
                    }
                }
                if(tyYNS.equals("Y") || tyYNS.equals("y")){
                    sqlQuery = sqlQuery + "Type";
                    if((secYesCheck - 1) != 0){
                        sqlQuery = sqlQuery + ", ";
                        secYesCheck -= 1;
                    }
                    else{
                        sqlQuery = sqlQuery + " ";
                    }
                }
                if(sYNS.equals("Y") || sYNS.equals("y")){
                    sqlQuery = sqlQuery + "Summary ";
                    secYesCheck -= 1;
                }
                sqlQuery = sqlQuery + "FROM Publications, Authors WHERE Publications.PublicationID = Authors.PublicationID AND ";
                if(!(tiS.equals("N") || tiS.equals("n"))){
                    sqlQuery = sqlQuery + "Title = " + "'" + tiS + "'";
                    if((yesCheck - 1) != 0){
                        sqlQuery = sqlQuery + " AND ";
                        yesCheck -= 1;
                    }
                }
                if(!(yS.equals("N") || yS.equals("n"))){
                    sqlQuery = sqlQuery + "Year = " + yS;
                    if((yesCheck - 1) != 0){
                        sqlQuery = sqlQuery + " AND ";
                        yesCheck -= 1;
                    }
                }
                if(!(aS.equals("N") || aS.equals("n"))){
                    sqlQuery = sqlQuery + "Author = " + "'" + aS + "'";
                    if((yesCheck - 1) != 0){
                        sqlQuery = sqlQuery + " AND ";
                        yesCheck -= 1;
                    }
                }
                if(!(tyS.equals("N") || tyS.equals("n"))){
                    sqlQuery = sqlQuery + "Type = " + "'" + tyS + "'";
                    yesCheck -= 1;
                }

                if(!(sorty.equals("N") || sorty.equals("n"))){
                    sqlQuery = sqlQuery + " ORDER BY " + sorty;
                }
                if(fYCheck == 0 || f2YCheck == 0){
                    if(fYCheck == 0){
                        System.out.println("You have left the input fields blank!");
                    }
                    if(f2YCheck == 0){
                        System.out.println("You have left the output fields blank!");
                    }
                }
                else{
                PreparedStatement pstmt = con.prepareStatement(sqlQuery);
                ResultSet rset = pstmt.executeQuery();
                int i = 1;
                ResultSetMetaData rsmd = rset.getMetaData();
                int j = rsmd.getColumnCount();
                int existo = 0;
                while(rset.next()){
                    existo = 1;
                    i = 1;
                    while(i != (j + 1)){
                        if(i == 1){
                            System.out.print(rset.getString(i));
                        }
                        else{
                            System.out.print(", ");
                            System.out.print(rset.getString(i));
                        }  
                        
                        i += 1;
                    }
                    System.out.println();
                }
                if(existo == 0){
                    System.out.println("That search query was not found!");
                }
                choice = 1;
                }
            }
            if(choice == 4){
                System.out.println("Thank you, goodbye!");
                System.exit(0);
            }
            
            }
            
        }catch( Exception e) {e.printStackTrace();}
    scan.close();
    scan2.close();

    }// End of connectToDatabase()
}// End of class