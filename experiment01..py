{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOPBwSwbEXwqXGIVQRUQ7NR",
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
        "<a href=\"https://colab.research.google.com/github/greeshmareddy98/MLA0201-FOML/blob/main/experiment01..py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wUi575WTMvwq",
        "outputId": "9ef5ce4c-546e-4473-86b2-83b1205bf29f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training Examples:\n",
            "['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']\n",
            "['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes']\n",
            "['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No']\n",
            "['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']\n",
            "\n",
            "Most Specific Hypothesis:\n",
            "['Sunny', 'Warm', '?', 'Strong', '?', '?']\n"
          ]
        }
      ],
      "source": [
        "data = [\n",
        "    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']\n",
        "]\n",
        "hypothesis = ['0', '0', '0', '0', '0', '0']\n",
        "\n",
        "for row in data:\n",
        "    if row[-1] == 'Yes':\n",
        "        for i in range(len(hypothesis)):\n",
        "            if hypothesis[i] == '0':\n",
        "                hypothesis[i] = row[i]\n",
        "            elif hypothesis[i] != row[i]:\n",
        "                hypothesis[i] = '?'\n",
        "print(\"Training Examples:\")\n",
        "for row in data:\n",
        "    print(row)\n",
        "print(\"\\nMost Specific Hypothesis:\")\n",
        "print(hypothesis)\n"
      ]
    }
  ]
}