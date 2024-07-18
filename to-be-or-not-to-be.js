var expect = function (val) {
  return {
    toBe: function (expected) {
      if (val === expected) {
        return true;
      } else {
        throw new Error(`Not Equal`);
      }
    },
    notToBe: (expected) => {
      if (val !== expected) {
        return true;
      } else {
        throw new Error(`Equal`);
      }
    },
  };
};

console.log(expect(5).notToBe(null));
