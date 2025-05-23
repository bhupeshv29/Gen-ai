class SimpleGPTTokenizer {
  constructor() {
    this.vocab = {};         // word → ID
    this.idToToken = {};     // ID → word
    this.nextId = 1;         // start token IDs from 1
  }

  // Split by space (or you can use regex for subword/character)
  tokenize(text) {
    return text.toLowerCase().trim().split(/\s+/);
  }

  // Build vocabulary and encode tokens
  encode(text) {
    const tokens = this.tokenize(text);
    const tokenIds = [];

    for (const token of tokens) {
      if (!(token in this.vocab)) {
        this.vocab[token] = this.nextId;
        this.idToToken[this.nextId] = token;
        this.nextId++;
      }
      tokenIds.push(this.vocab[token]);
    }

    return tokenIds;
  }

  // Convert token IDs back to text
  decode(tokenIds) {
    return tokenIds.map(id => this.idToToken[id] || "[UNK]").join(" ");
  }
}

// Example usage
const tokenizer = new SimpleGPTTokenizer();

const text = "hello world hello GPT";
const text1 = "helloo my name is bhupesh helloo name is my hello bhupesh"


const encoded = tokenizer.encode(text1);   // → [1, 2, 1, 3]
const decoded = tokenizer.decode(encoded); // → "hello world hello gpt"

console.log("Encoded:", encoded);
console.log("Decoded:", decoded);