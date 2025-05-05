import java.io.*;
import java.util.Properties;

public class LeggiJavaLauncher {
    public static void main(String[] args) {
        File file = new File("launcher.leggijava");

        if (!file.exists()) {
            System.out.println("❌ File .leggijava non trovato!");
            return;
        }

        try (FileReader reader = new FileReader(file)) {
            Properties props = new Properties();
            props.load(reader);

            System.out.println("🚀 Leggendo file .leggijava...");
            System.out.println("🧠 Main Class: " + props.getProperty("main_class"));
            System.out.println("💻 Memoria Allocata: " + props.getProperty("memory") + " MB");
            System.out.println("ℹ️  Versione: " + props.getProperty("version"));
            System.out.println("▶️  Args: " + props.getProperty("args"));

            System.out.println("✅ Lancio completato (simulato)");

        } catch (IOException e) {
            System.out.println("❌ Errore durante la lettura: " + e.getMessage());
        }
    }
}
