<template>
  <div>
    <h2>예약 페이지</h2>
    <h3>선생님 선택</h3>
    <button class="eric" 
    @click="selectEric"> Eric </button>  
    <button class="tony" @click="selectTony"> Tony </button>
    <hr>
    <h3>시간 선택</h3>
    <div class="table">
        <span class="time" 
        v-for="(time, index) in times" :key="index" 
        @click="timeSelect(time)"
        :class="{'selbtn':isSelected(time)}"
        >{{time}}</span>
    </div>  

    <button class="btn" @click="reservation"> 예약 확정 </button>
  </div>
</template>

<script>
export default {
    name:'TimeTable',
    data(){
        return{
            selectedTime:[],
            selectedTeacher:"",
            times: [
            "09:00","09:30","10:00","10:30","11:00","11:30",
            "12:00","12:30","13:00","13:30","14:00","14:30",
            "15:00","15:30","16:00","16:30","17:00","17:30",
                ],
        }
    },
    methods:{
       
        selectEric(){
            this.$emit('select-eric','Eric')
            this.selectedTeacher = 'Eric'
        },
        selectTony(){
            // 기억 안난부분 2, 데이터 emit에 담아 보내기
            this.$emit('select-tony','Tony')
            this.selectedTeacher = 'Tony'

        },
        timeSelect(time){
            if (this.selectedTime.includes(time)){
                const time_idx = this.selectedTime.indexOf(time);
                this.selectedTime.splice(time_idx, 1)
                return;
            }
            if (this.selectedTime.length >=5){
                alert('5타임까지만 신청할 수 있습니다.')
                return;
            }
            // 기억 안난 부분 1
            this.selectedTime.push(time)
            // console.log(this.selectedTime)
            this.$emit('time-select', this.selectedTime)
        },

        isSelected(time){
            if (this.selectedTime.includes(time)){
                return true;
            } else{
                return false;
            }
            
        },
        reservation(){
            if (!this.selectedTeacher){
                alert('선생님을 선택해 주세요!')
            } else{
                this.$emit('reservation', this.selectedTeacher)
            }
            if (this.selectedTime.length <1){
                alert('시간을 선택해 주세요!')
            } else{
                this.$emit('reservation', this.selectedTime)
            }
        }

}
}
</script>

<style>
.table{
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
.eric{
    width: 80px;
    height: 30px;
    border: solid 1px darkslategrey;
    margin: 10px;
}
.eric:hover{
    background-color: rgb(202, 229, 240);
}

.tony{
    width: 80px;
    height: 30px;
    border: solid 1px darkslategrey;
}

.tony:hover{
    background-color: rgb(202, 229, 240);
}

.selbtn{
    background-color: rgb(202, 229, 240);
    color: darkslateblue;
}

.btn {
    background-color: white;
    width: 80px;
    height: 30px;
    border: solid 1px darkslategrey;
}

</style>
