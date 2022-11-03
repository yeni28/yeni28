<template>
  <div id="app">
    <h1> SSAFY 상담 예약 시스템 </h1>
    <div class="whole">
      <section class="left">
        <h2>예약 페이지</h2>
        <div>
          <h3> 선생님 선택</h3>
          <div style="margin-bottom:10px;">
          <button class="btn1" @click="selteacherEric" :class="{'over':btn1}"> Eric </button> <button class="btn2" :class="{'over':btn2}" @click="selteacherTony"> Tony </button>
          </div>  
          <hr>
          <h3> 시간 선택 </h3>
          <div class="timetable">
          <span class="time" v-for="(time, index) in times" :key="index" @click="selectTime(time)" :class="{selectedbtn:isSelcted(time)}"> {{time}} </span>
          </div>
          <hr>
   
        </div>
      </section>
      <section class="right">
        <h2>상담 신청 현황</h2>
        <div>
          <h3> 상담 선생님</h3>
          <p> 성함 : {{ selectTeacher }} </p>
            <hr>
          <h3> 예약 현황 </h3>
          <p> 시간들 : <span v-for="time in selectTimes" :key="time">  {{time}}   </span></p>
          <hr>
          <img src="./assets/ssafy-logo.png" alt="SSAFY">
        </div>
      </section>
    </div>
  </div>
</template>

<script>



export default {
  name: 'App',
  components: {},
  data() {
    return{
      selectTeacher:"",
      selectTimes:[],
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30",
  "12:00","12:30","13:00","13:30","14:00","14:30",
  "15:00","15:30","16:00","16:30","17:00","17:30",
    ],
      btn1:false,
      btn2:false,
    }
  },
  methods:{
    selectTime(time){
      if (this.selectTimes.includes(time)){
        const time_idx=this.selectTimes.indexOf(time);
        this.selectTimes.splice(time_idx, 1);
        return;
      }

      if (this.selectTimes.length >= 5){
        alert('5타임까지만 신청할 수 있습니다.')
        return;
      }
      this.selectTimes.push(time)
      //push=append selectTimes라는 데이터값에 함수에서 받아온 time인자를 추가해주는 것이다.
    },
    isSelcted(time){
      if(this.selectTimes.includes(time)){
        return true;
      } else {
        false;
      }
    },
  
    selteacherEric(){
      this.selectTeacher = 'Eric'
      this.btn1= true;
      this.btn2= false;

    },
    selteacherTony(){
      this.selectTeacher = 'Tony'
      this.btn1= false;
      this.btn2= true;

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  font-family:'notosans';
}
.whole{
  display: flex;
  width: 800px;
  margin: auto;
  box-shadow: 20px 10px 20px  #d5d5d6;

}
.timetable{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 40px;
}
.time{
  margin: 5px;
  color: #a7a7a7;
}
.selectedbtn{
  background-color: #bfcdeb;
  color: #0F4C81;
}
.left{
  width: 50%;
  height: 450px;

}
.right{
  width: 50%;
  height: 450px;
  /* margin-left: auto; */
  /* margin-right: auto; */
  background-color: rgb(239, 246, 253);
}
.over{
  background-color: #bfcdeb;
}


.btn1{
  width: 80px;
  height: 30px;
  border: solid 1px #2c3e50;


}
.btn1:hover{
  background-color: #bfcdeb;

}
.btn2{
  width: 80px;
  height: 30px;
  border: solid 1px #2c3e50;

}
.btn2:hover{
  background-color: #bfcdeb;

}

@font-face {
  font-family:'notosans';
  src:url('./assets/fonts/NotoSansKR-Regular.otf')
}
hr{
  background-color: #2c3e50;
  border: 0;
  height: 1px;
  width: 80%;
}
</style>
