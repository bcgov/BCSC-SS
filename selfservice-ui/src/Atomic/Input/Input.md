This BC Input is amazing, use it responsibly.

## Examples

### Input

Text inputs allow users to enter a single line of text.

```js
<Input label='Input' counter='15' value='test'></Input>
```

<!-- Open console and start typing
click
```vue
import Vue from 'vue';
<template
  ><v-app>
    <Input label="input" @input="input" :value="value"></Input>
  </v-app>
</template>
<script>
export default {
  data() {
    return { value: '' };
  },
  methods: {
    input(val) {
      console.log('you typed value:', val);
    }
  }
};
</script>
``` -->
