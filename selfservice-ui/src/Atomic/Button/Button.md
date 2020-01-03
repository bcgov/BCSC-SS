This BC button is amazing, use it responsibly.

## Examples

### Primary button

Primary buttons allow users to carry out an important action on your service, such as Download or Submit.

```jsx
<Button>Primary Btn</Button>
```

Normal primary dark button:

```jsx
<div class='background-colour'>
  <Button dark>Dark Btn</Button>
</div>
```

### Secondary button

Secondary buttons allow users to carry out a supporting action on your service, such as Back or Cancel.

```jsx
<div>
  <Button secondary>secondary Btn</Button>
</div>
```

secondary button with dark and blue background:

```jsx
<div class='background-colour'>
  <Button secondary dark>
    Dark secondary Btn
  </Button>
</div>
```

### Disabled button

Disabled button :

```jsx
<div class='background-colour'>
  <Button disabled>Disabled</Button>
</div>
```

Disabled secondary button :

```jsx
<div class='background-colour'>
  <Button secondary disabled>
    secondary Disabled Btn
  </Button>
</div>
```

With on click action
click

```vue
<template>
  <Button @click="click">Click me</Button>
</template>
<script>
export default {
  methods: {
    click() {
      console.log('you pressed button');
    }
  }
};
</script>
```
