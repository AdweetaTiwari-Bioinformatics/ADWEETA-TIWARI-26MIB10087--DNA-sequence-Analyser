# ============================================================
# DNA CENTRAL DOGMA TOOLKIT
# ============================================================
#
# This program provides:
#
# 1. DNA sequence validation
# 2. DNA sequence analysis
# 3. Base counting
# 4. Base percentages
# 5. GC content
# 6. AT content
# 7. DNA complement
# 8. DNA reverse complement
# 9. DNA strand compatibility
# 10. DNA -> mRNA transcription
# 11. mRNA -> protein translation
# 12. DNA motif searching
# 13. Graphical User Interface (GUI)
# 14. Command Line Interface (CLI)
#===================================================================

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext


# ============================================================
# PART 1
# VALID DNA BASES
# ============================================================

VALID_DNA_BASES = set("ATGC")

VALID_MRNA_BASES = set("AUCG")


# ============================================================
# PART 2
# CODON TABLE
# ============================================================

CODON_TABLE = {

    "UUU": "F",
    "UUC": "F",

    "UUA": "L",
    "UUG": "L",

    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",

    "AUU": "I",
    "AUC": "I",
    "AUA": "I",

    "AUG": "M",

    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",

    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",

    "AGU": "S",
    "AGC": "S",

    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",

    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",

    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",

    "UAU": "Y",
    "UAC": "Y",

    "CAU": "H",
    "CAC": "H",

    "CAA": "Q",
    "CAG": "Q",

    "AAU": "N",
    "AAC": "N",

    "AAA": "K",
    "AAG": "K",

    "GAU": "D",
    "GAC": "D",

    "GAA": "E",
    "GAG": "E",

    "UGU": "C",
    "UGC": "C",

    "UGG": "W",

    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",

    "AGA": "R",
    "AGG": "R",

    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",

    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}


# ============================================================
# PART 3
# DNA CLEANING AND VALIDATION
# ============================================================

def clean_dna(sequence):

    sequence = sequence.strip().upper()

    return sequence


def validate_dna(sequence):

    sequence = clean_dna(sequence)

    if sequence == "":

        raise ValueError(
            "DNA sequence cannot be empty."
        )

    invalid_bases = set(sequence) - VALID_DNA_BASES

    if invalid_bases:

        invalid = ", ".join(
            sorted(invalid_bases)
        )

        raise ValueError(
            f"Invalid DNA base(s): {invalid}.\n"
            "Only A, T, G and C are allowed."
        )

    return sequence


# ============================================================
# PART 4
# DNA ANALYSIS
# ============================================================

def count_bases(sequence):

    sequence = validate_dna(sequence)

    counts = {

        "A": sequence.count("A"),

        "T": sequence.count("T"),

        "G": sequence.count("G"),

        "C": sequence.count("C")
    }

    return counts


def calculate_percentages(sequence):

    sequence = validate_dna(sequence)

    length = len(sequence)

    percentages = {

        "A":
        (sequence.count("A") / length) * 100,

        "T":
        (sequence.count("T") / length) * 100,

        "G":
        (sequence.count("G") / length) * 100,

        "C":
        (sequence.count("C") / length) * 100
    }

    return percentages


def calculate_gc_content(sequence):

    sequence = validate_dna(sequence)

    gc_count = (
        sequence.count("G")
        +
        sequence.count("C")
    )

    gc_percentage = (
        gc_count / len(sequence)
    ) * 100

    return gc_percentage


def calculate_at_content(sequence):

    sequence = validate_dna(sequence)

    at_count = (
        sequence.count("A")
        +
        sequence.count("T")
    )

    at_percentage = (
        at_count / len(sequence)
    ) * 100

    return at_percentage


def analyze_dna(sequence):

    sequence = validate_dna(sequence)

    result = {

        "sequence": sequence,

        "length": len(sequence),

        "counts":
        count_bases(sequence),

        "percentages":
        calculate_percentages(sequence),

        "GC":
        calculate_gc_content(sequence),

        "AT":
        calculate_at_content(sequence)
    }

    return result


# ============================================================
# PART 5
# DNA COMPLEMENT
# ============================================================

def complement(sequence):

    sequence = validate_dna(sequence)

    complement_map = {

        "A": "T",

        "T": "A",

        "G": "C",

        "C": "G"
    }

    result = ""

    for base in sequence:

        result += complement_map[base]

    return result


# ============================================================
# PART 6
# REVERSE COMPLEMENT
# ============================================================

def reverse_complement(sequence):

    sequence = validate_dna(sequence)

    complementary_sequence = complement(
        sequence
    )

    reversed_sequence = (
        complementary_sequence[::-1]
    )

    return reversed_sequence


# ============================================================
# PART 7
# DNA COMPATIBILITY
# ============================================================

def check_compatibility(
    strand1,
    strand2
):

    strand1 = validate_dna(strand1)

    strand2 = validate_dna(strand2)

    expected_strand = complement(
        strand1
    )

    return expected_strand == strand2


# ============================================================
# PART 8
# TRANSCRIPTION
# DNA TEMPLATE -> mRNA
# ============================================================

def transcribe(dna):

    dna = validate_dna(dna)

    transcription_map = {

        "A": "U",

        "T": "A",

        "G": "C",

        "C": "G"
    }

    mrna = ""

    for base in dna:

        mrna += transcription_map[base]

    return mrna


# ============================================================
# PART 9
# mRNA VALIDATION
# ============================================================

def clean_mrna(mrna):

    return mrna.strip().upper()


def validate_mrna(mrna):

    mrna = clean_mrna(mrna)

    if mrna == "":

        raise ValueError(
            "mRNA sequence cannot be empty."
        )

    invalid_bases = (
        set(mrna)
        -
        VALID_MRNA_BASES
    )

    if invalid_bases:

        invalid = ", ".join(
            sorted(invalid_bases)
        )

        raise ValueError(
            f"Invalid mRNA base(s): {invalid}.\n"
            "Only A, U, G and C are allowed."
        )

    return mrna


# ============================================================
# PART 10
# FIND START CODON
# ============================================================

def find_start_codon(mrna):

    mrna = validate_mrna(mrna)

    start_position = mrna.find("AUG")

    if start_position == -1:

        raise ValueError(
            "No AUG start codon was found."
        )

    return start_position


# ============================================================
# PART 11
# TRANSLATION
# mRNA -> PROTEIN
# ============================================================

def translate_mrna(mrna):

    mrna = validate_mrna(mrna)

    start_position = find_start_codon(
        mrna
    )

    protein = []

    for position in range(
        start_position,
        len(mrna) - 2,
        3
    ):

        codon = mrna[
            position:position + 3
        ]

        amino_acid = CODON_TABLE[
            codon
        ]

        if amino_acid == "STOP":

            break

        protein.append(
            amino_acid
        )

    if len(protein) == 0:

        raise ValueError(
            "No protein sequence could be generated."
        )

    return protein


def protein_to_string(protein):

    return "-".join(protein)


# ============================================================
# PART 12
# MOTIF VALIDATION
# ============================================================

def validate_motif(motif):

    motif = motif.strip().upper()

    if motif == "":

        raise ValueError(
            "Motif cannot be empty."
        )

    invalid_bases = (
        set(motif)
        -
        VALID_DNA_BASES
    )

    if invalid_bases:

        invalid = ", ".join(
            sorted(invalid_bases)
        )

        raise ValueError(
            f"Invalid motif base(s): {invalid}.\n"
            "A DNA motif can contain only A, T, G and C."
        )

    return motif


# ============================================================
# PART 13
# FIND MOTIF
# ============================================================

def find_motif(
    sequence,
    motif
):

    sequence = validate_dna(
        sequence
    )

    motif = validate_motif(
        motif
    )

    positions = []

    for position in range(
        len(sequence)
        -
        len(motif)
        +
        1
    ):

        current_section = sequence[
            position:
            position + len(motif)
        ]

        if current_section == motif:

            positions.append(
                position + 1
            )

    return positions


# ============================================================
# PART 14
# FORMAT DNA ANALYSIS
# ============================================================

def format_analysis(result):

    text = ""

    text += "DNA ANALYSIS\n"

    text += "============\n\n"

    text += (
        f"Sequence: "
        f"{result['sequence']}\n"
    )

    text += (
        f"Length: "
        f"{result['length']}\n\n"
    )

    text += "BASE COUNTS\n"

    text += "-----------\n"

    for base, count in (
        result["counts"].items()
    ):

        text += (
            f"{base}: {count}\n"
        )

    text += "\nBASE PERCENTAGES\n"

    text += "-----------------\n"

    for base, percentage in (
        result["percentages"].items()
    ):

        text += (
            f"{base}: "
            f"{percentage:.2f}%\n"
        )

    text += (
        f"\nGC Content: "
        f"{result['GC']:.2f}%\n"
    )

    text += (
        f"AT Content: "
        f"{result['AT']:.2f}%\n"
    )

    return text


# ============================================================
# PART 15
# COMMAND LINE INPUT HELPER
# ============================================================

def get_valid_dna_from_cli(
    prompt
):

    while True:

        try:

            sequence = input(
                prompt
            )

            return validate_dna(
                sequence
            )

        except ValueError as error:

            print()
            print(
                "❌ Invalid input."
            )

            print(
                error
            )

            print(
                "Please try again.\n"
            )


# ============================================================
# PART 16
# COMMAND LINE INTERFACE
# ============================================================

def run_cli():

    print()
    print("=" * 60)

    print(
        "        🧬 DNA CENTRAL DOGMA TOOLKIT"
    )

    print("=" * 60)

    print()

    print(
        "This toolkit follows:"
    )

    print(
        "DNA → mRNA → Protein"
    )

    print()


    # --------------------------------------------------------
    # GET FIRST DNA STRAND
    # --------------------------------------------------------

    strand1 = get_valid_dna_from_cli(
        "Enter DNA template strand: "
    )


    # --------------------------------------------------------
    # GET SECOND DNA STRAND
    # --------------------------------------------------------

    strand2 = get_valid_dna_from_cli(
        "Enter second DNA strand: "
    )


    while True:

        print()
        print("=" * 60)

        print(
            "MAIN MENU"
        )

        print("=" * 60)

        print(
            "1. Analyze DNA"
        )

        print(
            "2. Complement"
        )

        print(
            "3. Reverse Complement"
        )

        print(
            "4. Check Compatibility"
        )

        print(
            "5. Transcribe DNA → mRNA"
        )

        print(
            "6. Translate mRNA → Protein"
        )

        print(
            "7. Find DNA Motif"
        )

        print(
            "8. Enter New DNA Sequences"
        )

        print(
            "9. Exit"
        )

        print()


        choice = input(
            "Enter your choice: "
        ).strip()


        # ----------------------------------------------------
        # OPTION 1
        # ----------------------------------------------------

        if choice == "1":

            print()

            print(
                "========== STRAND 1 =========="
            )

            result1 = analyze_dna(
                strand1
            )

            print(
                format_analysis(
                    result1
                )
            )


            print(
                "========== STRAND 2 =========="
            )

            result2 = analyze_dna(
                strand2
            )

            print(
                format_analysis(
                    result2
                ))


        # ----------------------------------------------------
        # OPTION 2
        # ----------------------------------------------------

        elif choice == "2":

            result = complement(
                strand1
            )

            print()

            print(
                "DNA COMPLEMENT"
            )

            print(
                "=============="
            )

            print(
                f"Original: "
                f"{strand1}"
            )

            print(
                f"Complement: "
                f"{result}"
            )


        # ----------------------------------------------------
        # OPTION 3
        # ----------------------------------------------------

        elif choice == "3":

            result = reverse_complement(
                strand1
            )

            print()

            print(
                "REVERSE COMPLEMENT"
            )

            print(
                "=================="
            )

            print(
                f"Original: "
                f"{strand1}"
            )

            print(
                f"Reverse Complement: "
                f"{result}"
            )


        # ----------------------------------------------------
        # OPTION 4
        # ----------------------------------------------------

        elif choice == "4":

            compatible = check_compatibility(
                strand1,
                strand2
            )

            print()

            print(
                "DNA COMPATIBILITY"
            )

            print(
                "================="
            )

            print(
                f"Strand 1: "
                f"{strand1}"
            )

            print(
                f"Strand 2: "
                f"{strand2}"
            )

            if compatible:

                print(
                    "\n✓ The two strands "
                    "are complementary."
                )

            else:

                print(
                    "\n✗ The two strands "
                    "are not complementary."
                )


        # ----------------------------------------------------
        # OPTION 5
        # ----------------------------------------------------

        elif choice == "5":

            mrna = transcribe(
                strand1
            )

            print()

            print(
                "CENTRAL DOGMA"
            )

            print(
                "============="
            )

            print(
                f"DNA Template:\n"
                f"{strand1}"
            )

            print()

            print(
                "       ↓"
            )

            print(
                "TRANSCRIPTION"
            )

            print(
                "       ↓"
            )

            print()

            print(
                f"mRNA:\n"
                f"{mrna}"
            )


        # ----------------------------------------------------
        # OPTION 6
        # ----------------------------------------------------

        elif choice == "6":

            print()

            print(
                "Enter mRNA for translation."
            )

            while True:

                try:

                    mrna = input(
                        "mRNA: "
                    )

                    mrna = validate_mrna(
                        mrna
                    )

                    break

                except ValueError as error:

                    print()

                    print(
                        "❌ Invalid mRNA."
                    )

                    print(
                        error
                    )

                    print(
                        "Please try again."
                    )

            try:

                protein = translate_mrna(
                    mrna
                )

                protein_string = (
                    protein_to_string(
                        protein
                    )
                )

                print()

                print(
                    "CENTRAL DOGMA"
                )

                print(
                    "============="
                )

                print(
                    f"mRNA:\n"
                    f"{mrna}"
                )

                print()

                print(
                    "       ↓"
                )

                print(
                    "TRANSLATION"
                )

                print(
                    "       ↓"
                )

                print()

                print(
                    f"Protein:\n"
                    f"{protein_string}"
                )

            except ValueError as error:

                print()

                print(
                    "❌ Translation error:"
                )

                print(
                    error
                )


        # ----------------------------------------------------
        # OPTION 7
        # ----------------------------------------------------

        elif choice == "7":

            while True:

                try:

                    motif = input(
                        "Enter DNA motif: "
                    )

                    motif = validate_motif(
                        motif
                    )

                    break

                except ValueError as error:

                    print()

                    print(
                        "❌ Invalid motif."
                    )

                    print(
                        error
                    )


            positions1 = find_motif(
                strand1,
                motif
            )

            positions2 = find_motif(
                strand2,
                motif
            )

            print()

            print(
                "DNA MOTIF ANALYSIS"
            )

            print(
                "=================="
            )

            print(
                f"Motif: {motif}"
            )

            print()

            print(
                "STRAND 1"
            )

            print(
                f"Occurrences: "
                f"{len(positions1)}"
            )

            print(
                f"Positions: "
                f"{positions1}"
            )

            print()

            print(
                "STRAND 2"
            )

            print(
                f"Occurrences: "
                f"{len(positions2)}"
            )

            print(
                f"Positions: "
                f"{positions2}"
            )


        # ----------------------------------------------------
        # OPTION 8
        # ----------------------------------------------------

        elif choice == "8":

            print()

            print(
                "Enter new DNA sequences."
            )

            strand1 = (
                get_valid_dna_from_cli(
                    "New DNA template strand: "
                )
            )

            strand2 = (
                get_valid_dna_from_cli(
                    "New second DNA strand: "
                )
            )

            print(
                "\nDNA sequences updated."
            )


        # ----------------------------------------------------
        # OPTION 9
        # ----------------------------------------------------

        elif choice == "9":

            print()

            print(
                "Thank you for using "
                "the DNA Central Dogma Toolkit!"
            )

            print()

            break


        # ----------------------------------------------------
        # INVALID MENU CHOICE
        # ----------------------------------------------------

        else:

            print()

            print(
                "❌ Invalid choice."
            )

            print(
                "Please select a number from 1 to 9."
            )


# ============================================================
# PART 17
# GUI CLASS
# ============================================================

class DNAAnalyzerGUI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "🧬 DNA Central Dogma Toolkit"
        )

        self.root.geometry(
            "950x850"
        )


        # ====================================================
        # TITLE
        # ====================================================

        title = tk.Label(
            root,
            text="🧬 DNA Central Dogma Toolkit",
            font=(
                "Arial",
                24,
                "bold"
            )
        )

        title.pack(
            pady=15
        )


        subtitle = tk.Label(
            root,
            text=(
                "DNA → Transcription → mRNA "
                "→ Translation → Protein"
            ),
            font=(
                "Arial",
                13
            )
        )

        subtitle.pack(
            pady=5
        )


        # ====================================================
        # DNA INPUT
        # ====================================================

        input_frame = tk.LabelFrame(
            root,
            text="DNA Input",
            font=(
                "Arial",
                12,
                "bold"
            ),
            padx=10,
            pady=10
        )

        input_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )


        # FIRST DNA STRAND

        tk.Label(
            input_frame,
            text="DNA Template Strand:"
        ).pack()


        self.strand1_entry = tk.Entry(
            input_frame,
            width=85,
            font=(
                "Arial",
                12
            )
        )

        self.strand1_entry.pack(
            pady=5
        )


        # SECOND DNA STRAND

        tk.Label(
            input_frame,
            text="Second DNA Strand:"
        ).pack()


        self.strand2_entry = tk.Entry(
            input_frame,
            width=85,
            font=(
                "Arial",
                12
            )
        )

        self.strand2_entry.pack(
            pady=5
        )


        # ====================================================
        # DNA ANALYSIS
        # ====================================================

        analysis_frame = tk.LabelFrame(
            root,
            text="DNA Analysis & Operations",
            font=(
                "Arial",
                12,
                "bold"
            ),
            padx=10,
            pady=10
        )

        analysis_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )


        tk.Button(
            analysis_frame,
            text="Analyze DNA",
            command=self.gui_analyze,
            width=18
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )


        tk.Button(
            analysis_frame,
            text="Complement",
            command=self.gui_complement,
            width=18
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )


        tk.Button(
            analysis_frame,
            text="Reverse Complement",
            command=self.gui_reverse_complement,
            width=18
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )


        tk.Button(
            analysis_frame,
            text="Check Compatibility",
            command=self.gui_compatibility,
            width=18
        ).grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )


        # ====================================================
        # CENTRAL DOGMA
        # ====================================================

        dogma_frame = tk.LabelFrame(
            root,
            text="Central Dogma",
            font=(
                "Arial",
                12,
                "bold"
            ),
            padx=10,
            pady=10
        )

        dogma_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )


        tk.Button(
            dogma_frame,
            text="DNA → mRNA\nTRANSCRIBE",
            command=self.gui_transcribe,
            width=22,
            height=3
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=5
        )


        tk.Button(
            dogma_frame,
            text="mRNA → Protein\nTRANSLATE",
            command=self.gui_translate,
            width=22,
            height=3
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=5
        )


        # ====================================================
        # MOTIF ANALYSIS
        # ====================================================

        motif_frame = tk.LabelFrame(
            root,
            text="Motif Analysis",
            font=(
                "Arial",
                12,
                "bold"
            ),
            padx=10,
            pady=10
        )

        motif_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )


        tk.Label(
            motif_frame,
            text="DNA Motif:"
        ).grid(
            row=0,
            column=0,
            padx=5
        )


        self.motif_entry = tk.Entry(
            motif_frame,
            width=25
        )

        self.motif_entry.grid(
            row=0,
            column=1,
            padx=5
        )


        tk.Button(
            motif_frame,
            text="Find Motif",
            command=self.gui_motif,
            width=15
        ).grid(
            row=0,
            column=2,
            padx=5
        )


        # ====================================================
        # RESULTS
        # ====================================================

        result_frame = tk.LabelFrame(
            root,
            text="Results",
            font=(
                "Arial",
                12,
                "bold"
            ),
            padx=10,
            pady=10
        )

        result_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )


        self.output = scrolledtext.ScrolledText(
            result_frame,
            width=105,
            height=20,
            font=(
                "Courier New",
                10
            )
        )

        self.output.pack(
            fill="both",
            expand=True
        )


        # ====================================================
        # CLEAR
        # ====================================================

        tk.Button(
            root,
            text="Clear",
            command=self.gui_clear,
            width=15
        ).pack(
            pady=10
        )


    # ========================================================
    # GET STRAND 1
    # ========================================================

    def get_gui_strand1(self):

        strand = (
            self.strand1_entry.get()
        )

        if not strand.strip():

            raise ValueError(
                "Please enter DNA Template Strand."
            )

        return validate_dna(
            strand
        )


    # ========================================================
    # GET BOTH STRANDS
    # ========================================================

    def get_gui_both_strands(self):

        strand1 = (
            self.strand1_entry.get()
        )

        strand2 = (
            self.strand2_entry.get()
        )


        if not strand1.strip():

            raise ValueError(
                "Please enter DNA Template Strand."
            )


        if not strand2.strip():

            raise ValueError(
                "Please enter Second DNA Strand."
            )


        strand1 = validate_dna(
            strand1
        )

        strand2 = validate_dna(
            strand2
        )


        return strand1, strand2


    # ========================================================
    # ANALYZE
    # ========================================================

    def gui_analyze(self):

        try:

            strand1, strand2 = (
                self.get_gui_both_strands()
            )


            result1 = analyze_dna(
                strand1
            )

            result2 = analyze_dna(
                strand2
            )


            self.output.delete(
                "1.0",
                tk.END
            )


            self.output.insert(
                tk.END,
                "========================================\n"
            )

            self.output.insert(
                tk.END,
                "              STRAND 1\n"
            )

            self.output.insert(
                tk.END,
                "========================================\n\n"
            )


            self.output.insert(
                tk.END,
                format_analysis(
                    result1
                )
            )


            self.output.insert(
                tk.END,
                "\n\n"
            )


            self.output.insert(
                tk.END,
                "========================================\n"
            )

            self.output.insert(
                tk.END,
                "              STRAND 2\n"
            )

            self.output.insert(
                tk.END,
                "========================================\n\n"
            )


            self.output.insert(
                tk.END,
                format_analysis(
                    result2
                )
            )


        except ValueError as error:

            messagebox.showerror(
                "Invalid DNA",
                str(error)
            )


    # ========================================================
    # COMPLEMENT
    # ========================================================

    def gui_complement(self):

        try:

            strand = (
                self.get_gui_strand1()
            )

            result = complement(
                strand
            )


            self.output.delete(
                "1.0",
                tk.END
            )


            self.output.insert(
                tk.END,
                "DNA COMPLEMENT\n"
            )

            self.output.insert(
                tk.END,
                "===============\n\n"
            )

            self.output.insert(
                tk.END,
                f"DNA:\n{strand}\n\n"
            )

            self.output.insert(
                tk.END,
                f"Complement:\n{result}\n"
            )


        except ValueError as error:

            messagebox.showerror(
                "Invalid DNA",
                str(error)
            )


    # ========================================================
    # REVERSE COMPLEMENT
    # ========================================================

    def gui_reverse_complement(
        self
    ):

        try:

            strand = (
                self.get_gui_strand1()
            )

            result = (
                reverse_complement(
                    strand
                )
            )


            self.output.delete(
                "1.0",
                tk.END
            )


            self.output.insert(
                tk.END,
                "DNA REVERSE COMPLEMENT\n"
            )

            self.output.insert(
                tk.END,
                "=======================\n\n"
            )

            self.output.insert(
                tk.END,
                f"DNA:\n{strand}\n\n"
            )

            self.output.insert(
                tk.END,
                f"Reverse Complement:\n{result}\n"
            )


        except ValueError as error:

            messagebox.showerror(
                "Invalid DNA",
                str(error)
            )


    # ========================================================
    # COMPATIBILITY
    # ========================================================

    def gui_compatibility(
        self
    ):

        try:

            strand1, strand2 = (
                self.get_gui_both_strands()
            )


            compatible = (
                check_compatibility(
                    strand1,
                    strand2
                )
            )


            self.output.delete(
                "1.0",
                tk.END
            )


            self.output.insert(
                tk.END,
                "DNA COMPATIBILITY\n"
            )

            self.output.insert(
                tk.END,
                "=================\n\n"
            )


            self.output.insert(
                tk.END,
                f"Strand 1:\n"
                f"{strand1}\n\n"
            )


            self.output.insert(
                tk.END,
                f"Strand 2:\n"
                f"{strand2}\n\n"
            )


            if compatible:

                self.output.insert(
                    tk.END,
                    "✓ The two strands "
                    "are complementary."
                )

            else:

                self.output.insert(
                    tk.END,
                    "✗ The two strands "
                    "are not complementary."
                )


        except ValueError as error:

            messagebox.showerror(
                "Compatibility Error",
                str(error)
            )


    # ========================================================
    # TRANSCRIPTION
    # ========================================================

    def gui_transcribe(
        self
    ):

        try:

            dna = (
                self.get_gui_strand1()
            )

            mrna = transcribe(
                dna
            )


            self.output.delete(
                "1.0",
                tk.END
            )


            self.output.insert(
                tk.END,
                "========================================\n"
            )

            self.output.insert(
                tk.END,
                "       CENTRAL DOGMA: TRANSCRIPTION\n"
            )

            self.output.insert(
                tk.END,
                "========================================\n\n"
            )


            self.output.insert(
                tk.END,
                "DNA TEMPLATE\n"
            )

            self.output.insert(
                tk.END,
                f"{dna}\n\n"
            )


            self.output.insert(
                tk.END,
                "              ↓\n"
            )

            self.output.insert(
                tk.END,
                "        TRANSCRIPTION\n"
            )

            self.output.insert(
                tk.END,
                "              ↓\n\n"
            )


            self.output.insert(
                tk.END,
                "mRNA\n"
            )

            self.output.insert(
                tk.END,
                f"{mrna}\n"
            )


        except ValueError as error:

            messagebox.showerror(
                "Transcription Error",
                str(error)
            )


    # ========================================================
    # TRANSLATION
    # ========================================================

    def gui_translate(
        self
    ):

        try:

            mrna = (
                self.get_gui_mrna()
            )

            protein = (
                translate_mrna(
                    mrna
                )
            )

            protein_string = (
                protein_to_string(
                    protein
                )
            )


            self.output.delete(
                "1.0",
                tk.END
            )


            self.output.insert(
                tk.END,
                "========================================\n"
            )

            self.output.insert(
                tk.END,
                "        CENTRAL DOGMA: TRANSLATION\n"
            )

            self.output.insert(
                tk.END,
                "========================================\n\n"
            )


            self.output.insert(
                tk.END,
                "mRNA\n"
            )

            self.output.insert(
                tk.END,
                f"{mrna}\n\n"
            )


            self.output.insert(
                tk.END,
                "              ↓\n"
            )

            self.output.insert(
                tk.END,
                "          TRANSLATION\n"
            )

            self.output.insert(
                tk.END,
                "              ↓\n\n"
            )


            self.output.insert(
                tk.END,
                "PROTEIN\n"
            )

            self.output.insert(
                tk.END,
                f"{protein_string}\n"
            )


        except ValueError as error:

            messagebox.showerror(
                "Translation Error",
                str(error)
            )


    # ========================================================
    # GET mRNA FOR TRANSLATION
    # ========================================================

    def get_gui_mrna(self):

        mrna = (
            self.strand1_entry.get()
        )

        if not mrna.strip():

            raise ValueError(
                "Enter mRNA in the first input box "
                "before translating."
            )

        return validate_mrna(
            mrna
        )


    # ========================================================
    # MOTIF
    # ========================================================

    def gui_motif(self):

        try:

            strand1, strand2 = (
                self.get_gui_both_strands()
            )

            motif = (
                self.motif_entry.get()
            )


            motif = validate_motif(
                motif
            )


            positions1 = find_motif(
                strand1,
                motif
            )

            positions2 = find_motif(
                strand2,
                motif
            )


            self.output.delete(
                "1.0",
                tk.END
            )


            self.output.insert(
                tk.END,
                "DNA MOTIF ANALYSIS\n"
            )

            self.output.insert(
                tk.END,
                "==================\n\n"
            )


            self.output.insert(
                tk.END,
                f"Motif: {motif}\n\n"
            )


            self.output.insert(
                tk.END,
                "STRAND 1\n"
            )

            self.output.insert(
                tk.END,
                f"Occurrences: "
                f"{len(positions1)}\n"
            )

            self.output.insert(
                tk.END,
                f"Positions: "
                f"{positions1}\n\n"
            )


            self.output.insert(
                tk.END,
                "STRAND 2\n"
            )

            self.output.insert(
                tk.END,
                f"Occurrences: "
                f"{len(positions2)}\n"
            )

            self.output.insert(
                tk.END,
                f"Positions: "
                f"{positions2}\n"
            )


        except ValueError as error:

            messagebox.showerror(
                "Motif Error",
                str(error)
            )


    # ========================================================
    # CLEAR
    # ========================================================

    def gui_clear(
        self
    ):

        self.strand1_entry.delete(
            0,
            tk.END
        )

        self.strand2_entry.delete(
            0,
            tk.END
        )

        self.motif_entry.delete(
            0,
            tk.END
        )

        self.output.delete(
            "1.0",
            tk.END
        )


# ============================================================
# PART 18
# START GUI
# ============================================================

def start_gui():

    root = tk.Tk()

    DNAAnalyzerGUI(
        root
    )

    root.mainloop()


# ============================================================
# PART 19
# MAIN PROGRAM
# ============================================================

def main():

    print()
    print("=" * 60)

    print(
        "        🧬 DNA CENTRAL DOGMA TOOLKIT"
    )

    print("=" * 60)

    print()

    print(
        "Choose how you want to run the toolkit:"
    )

    print()

    print(
        "1. Graphical Interface"
    )

    print(
        "2. Command Line Interface"
    )

    print(
        "3. Exit"
    )

    print()


    while True:

        choice = input(
            "Enter your choice: "
        ).strip()


        if choice == "1":

            start_gui()

            break


        elif choice == "2":

            run_cli()

            break


        elif choice == "3":

            print(
                "Goodbye!"
            )

            break


        else:

            print()

            print(
                "❌ Invalid choice."
            )

            print(
                "Please enter 1, 2 or 3."
            )

            print()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()