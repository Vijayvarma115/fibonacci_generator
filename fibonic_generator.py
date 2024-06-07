import matplotlib.pyplot as plt

def generate_fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def save_to_file(sequence, filename="fibonacci_sequence.txt"):
    with open(filename, 'w') as f:
        for number in sequence:
            f.write(f"{number}\n")
    print(f"Sequence saved to {filename}")

def plot_fibonacci(sequence):
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title('Fibonacci Sequence')
    plt.xlabel('Index')
    plt.ylabel('Fibonacci Number')
    plt.grid(True)
    plt.show()

def main():
    print("Welcome to the Fibonacci Generator!")
    try:
        num_terms = int(input("Enter the number of terms you want to generate: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
            return

        fib_sequence = generate_fibonacci(num_terms)
        print(f"Generated Fibonacci sequence: {fib_sequence}")

        save_to_file(fib_sequence)
        plot_fibonacci(fib_sequence)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
