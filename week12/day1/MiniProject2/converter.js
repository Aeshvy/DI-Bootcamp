const API_KEY = "17d23dca09d7f4ab1c577b3c";
const fromCurrency = document.getElementById("fromCurrency");
const toCurrency = document.getElementById("toCurrency");
const amountInput = document.getElementById("amount");
const resultDiv = document.getElementById("result");

async function fetchCurrencies() {
  try {
    const res = await fetch(
      `https://v6.exchangerate-api.com/v6/${API_KEY}/codes`
    );
    const data = await res.json();
    if (data.result !== "success")
      throw new Error(data["error-type"] || "Failed to fetch currencies");

    data.supported_codes.forEach(([code, name]) => {
      const optionFrom = new Option(`${code} - ${name}`, code);
      const optionTo = new Option(`${code} - ${name}`, code);
      fromCurrency.add(optionFrom);
      toCurrency.add(optionTo);
    });
    fromCurrency.value = "USD";
    toCurrency.value = "ILS";
  } catch (err) {
    resultDiv.innerText = "Error loading currencies: " + err.message;
  }
}

async function convert() {
  try {
    const from = fromCurrency.value;
    const to = toCurrency.value;
    const amount = amountInput.value;

    if (!amount || isNaN(amount) || amount <= 0) {
      resultDiv.innerText = "Please enter a valid amount.";
      return;
    }

    const res = await fetch(
      `https://v6.exchangerate-api.com/v6/${API_KEY}/pair/${from}/${to}/${amount}`
    );
    const data = await res.json();

    if (data.result !== "success") {
      throw new Error(data["error-type"] || "Conversion failed");
    }

    resultDiv.innerText = `${data.conversion_result} ${to}`;
  } catch (err) {
    resultDiv.innerText = "Error during conversion: " + err.message;
  }
}


function switchCurrencies() {
  const temp = fromCurrency.value;
  fromCurrency.value = toCurrency.value;
  toCurrency.value = temp;
  convert();
}



fetchCurrencies();
