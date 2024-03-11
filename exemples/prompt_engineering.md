
 # Rendre ces prompts directifs


```java
// Add a function that calculate prime numbers between two values. Think step by step
public class PrimeNumberUtils {
  public static List<Integer> getPrimeNumbers(int start, int end) {
    List<Integer> primeNumbers = new ArrayList<>();

    for (int i = start; i <= end; i++) {
      if (isPrime(i)) {
        primeNumbers.add(i);
      }
    }

    return primeNumbers;
  }

  private static boolean isPrime(int number) {
    if (number <= 1) {
      return false;
    }

    for (int i = 2; i < number; i++) {
      if (number % i == 0) {
        return false;
      }
    }

    return true;
  }
}
```


```java
// Méthode prenant en entrée deux nombres et retournant une liste de nombre premier entre ces deux nombres. La méthode throw une exception dans les cas invalides.
public List<Integer> getPrimeNumbers(int start, int end) {
	if (start < 0 || end < 0) {
	  throw new IllegalArgumentException("The start and end numbers must be positive");
	}
	
	if (start > end) {
	  throw new IllegalArgumentException("The start number must be less than the end number");
	}
	
	List<Integer> primeNumbers = new ArrayList<>();
	
	for (int i = start; i <= end; i++) {
	  if (Boolean.TRUE.equals(isPrime(i))) {
		primeNumbers.add(i);
	  }
	}
	
	return primeNumbers;
}

private Boolean isPrime(int number) {
	if (number <= 1) {
	  return false;
	}
	
	for (int i = 2; i <= Math.sqrt(number); i++) {
	  if (number % i == 0) {
		return false;
	  }
	}
	
	return true;
}
```