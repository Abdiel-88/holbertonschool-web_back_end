module.exports = {
    "env": {
        "node": true, // Updated to specify Node.js environment
        "es6": true
    },
    "extends": "eslint:recommended",
    "globals": {
        "Atomics": "readonly",
        "SharedArrayBuffer": "readonly"
    },
    "parserOptions": {
        "ecmaVersion": 2018,
        "sourceType": "module"
    },
    "rules": {
        // Example rules (uncomment to apply)
        // "no-unused-vars": "warn", // Warns on unused variables
        // "eqeqeq": ["error", "always"], // Enforces strict equality
    }
};
