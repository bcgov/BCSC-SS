This BC Select is amazing, use it responsibly.

## Examples

### Select

Text Selects allow users to enter a single line of text.

```js
<Select label='input' value='test'></Select>
```

<!-- Open console and start typing
click
```vue
import Vue from 'vue';
<template
  ><v-app>
    <Select label="Select" @input="input" :value="value"></Select>
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
