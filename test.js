const assert = require('assert')

describe('HelloWorld Module', () => {
  it('should return -1 when "Hello" is missing', function () {
    assert.equal(0, 'Hallo World'.indexOf('Hello'));
  });
  it('should return 0 when sentence starts with Hello', () => {
    assert.equal(0, 'Hello World, how are you?'.indexOf('Hello'));
  });
});
