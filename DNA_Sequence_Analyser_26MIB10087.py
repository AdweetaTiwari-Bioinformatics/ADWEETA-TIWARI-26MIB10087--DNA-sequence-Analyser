{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNYRZxdgG3hH0iv1acLSDn/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AdweetaTiwari-Bioinformatics/ADWEETA-TIWARI-26MIB10087--DNA-sequence-Analyser/blob/main/python_programs.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def analyze_sequence(sequence):\n",
        "\n",
        "    length = len(sequence)\n",
        "\n",
        "    a_count = sequence.count(\"A\")\n",
        "    t_count = sequence.count(\"T\")\n",
        "    g_count = sequence.count(\"G\")\n",
        "    c_count = sequence.count(\"C\")\n",
        "\n",
        "    a_percentage = (a_count / length) * 100\n",
        "    t_percentage = (t_count / length) * 100\n",
        "    g_percentage = (g_count / length) * 100\n",
        "    c_percentage = (c_count / length) * 100\n",
        "\n",
        "    gc_content = ((g_count + c_count) / length) * 100\n",
        "    at_content = ((a_count + t_count) / length) * 100\n",
        "\n",
        "    print(\"Length:\", length)\n",
        "\n",
        "    print(\"A:\", a_count)\n",
        "    print(\"T:\", t_count)\n",
        "    print(\"G:\", g_count)\n",
        "    print(\"C:\", c_count)\n",
        "\n",
        "    print(\"A percentage:\", round(a_percentage, 2), \"%\")\n",
        "    print(\"T percentage:\", round(t_percentage, 2), \"%\")\n",
        "    print(\"G percentage:\", round(g_percentage, 2), \"%\")\n",
        "    print(\"C percentage:\", round(c_percentage, 2), \"%\")\n",
        "\n",
        "    print(\"GC Content:\", round(gc_content, 2), \"%\")\n",
        "    print(\"AT Content:\", round(at_content, 2), \"%\")\n",
        "\n",
        "print(\"====================================\")\n",
        "print(\"       DNA sequence anlyser         \")\n",
        "print(\"====================================\")\n",
        "\n",
        "\n",
        "strand1 = input(\"Enter first DNA strand: \").upper()\n",
        "\n",
        "print(\"\\n===== STRAND 1 ANALYSIS =====\")\n",
        "analyze_sequence(strand1)\n",
        "\n",
        "strand2 = input(\"\\nEnter second DNA strand: \").upper()\n",
        "\n",
        "print(\"\\n===== STRAND 2 ANALYSIS =====\")\n",
        "analyze_sequence(strand2)\n",
        "\n",
        "complement = \"\"\n",
        "\n",
        "for base in strand1:\n",
        "    if base == \"A\":\n",
        "        complement += \"T\"\n",
        "    elif base == \"T\":\n",
        "        complement += \"A\"\n",
        "    elif base == \"G\":\n",
        "        complement += \"C\"\n",
        "    elif base == \"C\":\n",
        "        complement += \"G\"\n",
        "\n",
        "print(\"\\n===== COMPARISON =====\")\n",
        "\n",
        "print(\"Strand 1:\", strand1)\n",
        "print(\"Strand 2:\", strand2)\n",
        "print(\"Complement of Strand 1:\", complement)\n",
        "\n",
        "if complement == strand2:\n",
        "    print(\"Result: The two strands are complementary!\")\n",
        "else:\n",
        "    print(\"Result: The two strands are NOT complementary.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gVMdWPm-JHzG",
        "outputId": "8039a176-6612-4e85-e774-361f2e45a7f4"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "====================================\n",
            "       DNA sequence anlyser         \n",
            "====================================\n",
            "Enter first DNA strand: atgc\n",
            "\n",
            "===== STRAND 1 ANALYSIS =====\n",
            "Length: 4\n",
            "A: 1\n",
            "T: 1\n",
            "G: 1\n",
            "C: 1\n",
            "A percentage: 25.0 %\n",
            "T percentage: 25.0 %\n",
            "G percentage: 25.0 %\n",
            "C percentage: 25.0 %\n",
            "GC Content: 50.0 %\n",
            "AT Content: 50.0 %\n",
            "\n",
            "Enter second DNA strand: tacg\n",
            "\n",
            "===== STRAND 2 ANALYSIS =====\n",
            "Length: 4\n",
            "A: 1\n",
            "T: 1\n",
            "G: 1\n",
            "C: 1\n",
            "A percentage: 25.0 %\n",
            "T percentage: 25.0 %\n",
            "G percentage: 25.0 %\n",
            "C percentage: 25.0 %\n",
            "GC Content: 50.0 %\n",
            "AT Content: 50.0 %\n",
            "\n",
            "===== COMPARISON =====\n",
            "Strand 1: ATGC\n",
            "Strand 2: TACG\n",
            "Complement of Strand 1: TACG\n",
            "Result: The two strands are complementary!\n"
          ]
        }
      ]
    }
  ]
}
