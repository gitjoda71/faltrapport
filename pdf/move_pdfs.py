import os
import shutil
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import pypdf
except ImportError:
    try:
        import PyPDF2 as pypdf
    except ImportError:
        install('pypdf')
        import pypdf

def contains_keyword(pdf_path, keywords):
    try:
        with open(pdf_path, 'rb') as f:
            reader = pypdf.PdfReader(f)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_lower = text.lower()
                    if any(kw.lower() in text_lower for kw in keywords):
                        return True
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return False

def main():
    target_dir = r"C:\0-Dropbox\Dropbox\1oels dokument\Antigravity\hv\pdf"
    new_dir = os.path.join(target_dir, "personnummer_joel")
    
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        
    keywords = ["personnummer", "Joel"]
    moved_count = 0
    
    for filename in os.listdir(target_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(target_dir, filename)
            if contains_keyword(filepath, keywords):
                print(f"Moving {filename}...")
                try:
                    shutil.move(filepath, os.path.join(new_dir, filename))
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {filename}: {e}")
                
    print(f"Moved {moved_count} files.")

if __name__ == "__main__":
    main()
