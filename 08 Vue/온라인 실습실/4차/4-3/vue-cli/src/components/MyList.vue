<template>
  <div>
    <h2>상담 신청 현황</h2>
    <h3>상담 선생님</h3>
    <p>성함 : {{selectedTeacher }}</p>
    <hr>
    <h3>예약 현황</h3>
    <p> 시간들 : <span v-for="time in selectTime" :key="time">{{time }} </span> </p>
    <hr>

  </div>
</template>

<script>
export default {
    name:'MyList',
    props:{
        selectedTeacher: String,
        selectTime : Array,
    }
}
</script>

<style>

</style>