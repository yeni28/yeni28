<template>
  <div>
    <input type="text"
      v-model="todoTitle"
      @keyup.enter="createdTodo"
    >
  </div>
</template>

<script>
export default {
    name:'TodoForm',
    data: function(){
        return {
            todoTitle: null,
        }
    },
    methods:{
        createdTodo : function(){
            this.$emit('create-todo', this.todoTitle)
            this.todoTitle = null
        }
    }
}
</script>

<style>

</style>