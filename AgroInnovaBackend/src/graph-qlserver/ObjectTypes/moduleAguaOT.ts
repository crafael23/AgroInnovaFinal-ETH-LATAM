/* eslint-disable @typescript-eslint/no-unused-vars */
import { Field, Float, Int, ObjectType } from '@nestjs/graphql';

@ObjectType()
export class moduleAguaOT {
  @Field(() => Int)
  id: number;

  @Field(() => Float)
  nivel: number;

  @Field(() => Float)
  ph: number;

  @Field(() => Boolean)
  pumpState: boolean;

  @Field(() => Date)
  dateTime: Date;
}
