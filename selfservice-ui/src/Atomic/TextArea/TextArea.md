This BC TextArea is amazing, use it responsibly.

## Examples

### TextArea

Text TextAreas allow users to enter a single line of text.

```js
<TextArea label='input' value='test'></TextArea>
```

<!-- Open console and start typing
click
```vue
import Vue from 'vue';
<template
  ><v-app>
    <TextArea label="TextArea" @input="input" :value="value"></TextArea>
  </v-app>
</template>
<script>
export default {
  data() {
    return { value: '' };
  },
  methods: {
    TextArea(val) {
      console.log('you typed value:', val);
    }
  }
};
</script>
``` -->
