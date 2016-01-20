//State lsit
//Pan servo possible motion : Right left AS Right + left - Basend on a reference angle compared to the north pole 0 = dont move
//Tilt servo. Max 90deg up min 0  : + = up and - = down 0 = dont move

#define DONT_MOVE 0
#define PANU_TILTN 1
#define PANU_TILTD 2
#define PANU_TILTU 3
#define PAND_TILTN 4
#define PAND_TILTD 5
#define PAND_TILTU 6
#define PANN_TILTU 7
#define PANN_TILTD 8


int state;

int move_servos(){
	switch (state){

		case (DONT_MOVE):
			servo_rot(HOLD,HOLD);
		break;

		case (PANU_TILTN):
			servo_rot(UP,HOLD);
		break;

		case (PANU_TILTD):
			servo_rot(UP,DOWN);
		break;

		case (PANU_TILTU):
			servo_rot(UP,UP);
		break;

		case (PAND_TILTN):
			servo_rot(DOWN,HOLD);
		break;

		case (PAND_TILTD):
			servo_rot(DOWN,DOWN);
		break;

		case (PAND_TILTU):
			servo_rot(DOWN,UP);
		break;

		case (PANN_TILTD):
			servo_rot(HOlD,DOWN);
		break;

		case (PANN_TILTU):
			servo_rot(HOLD,UP);
		break;

	}

	return state;
}

int change_state(void){

	
	//360 deg max movement
	//0-90 deg pan max



}