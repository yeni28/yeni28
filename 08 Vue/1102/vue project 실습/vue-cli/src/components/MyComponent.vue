<template>
  <div>
    <h1> 새로 생성한 컴포넌트 </h1>
    <MyComponentItem/>
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem.vue';
// 차후 import를 위해서
export default {
    name : 'MyComponent',
    components:{
        MyComponentItem
    },
}
</script>

<style>
    
</style>