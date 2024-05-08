module.exports = {
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
      globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly'
      }
    },
    plugins: {
      jest: require('eslint-plugin-jest'),
    },
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement'
      ],
      'eqeqeq': ['error', 'always'],  // Enforce the use of === and !==
      'no-var': 'error',              // Require let or const instead of var
      'prefer-const': 'error',        // Suggest using const
      'no-unused-vars': 'warn',       // Warn about variables that are declared but not used
      'no-undef': 'error',            // Disallow undeclared variables
      'consistent-return': 'error'    // Require return statements to either always or never specify values
    },
    linterOptions: {
      envs: ['node', 'jest']
    }
  };
  