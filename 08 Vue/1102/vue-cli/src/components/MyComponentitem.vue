<template>
  <div>
    <h3> 나는 MyComponent의 하위 컴포넌트야 </h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent"> 클릭</button>
    <input type="text" 
    v-model="childInputData"
    @keyup.enter="childInput">
  </div>
</template>

<script>


export default {
    name: 'MyComponentitem',
    props:{
        staticProps: String,
        dynamicProps: String,
    },
    methods:{
        childToParent: function () {
            this.$emit('child-to-parent', '나는 자식이 보낸 데이터다')
        },
        childInput: function(){
            this.$emit('child-input',this.childInputData)
            this.childInputData = null
        }
    },
    data: function(){
        return {
            childInputData: null,
        }
    },

}
</script>

<style>


</style>