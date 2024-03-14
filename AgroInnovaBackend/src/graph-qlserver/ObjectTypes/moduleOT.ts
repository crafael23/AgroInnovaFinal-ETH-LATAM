import { Field, Float, Int, ObjectType } from '@nestjs/graphql';

/* eslint-disable @typescript-eslint/no-unused-vars */

@ObjectType()
export class ModuleOT {
  @Field(() => Int, { nullable: true })
  id: number;

  @Field(() => Int, { nullable: true })
  moduleId: number;

  @Field(() => Float, { nullable: true })
  temperature: number;

  @Field(() => Float, { nullable: true })
  humidity: number;

  @Field(() => Boolean, { nullable: true })
  valve: boolean;

  @Field(() => Date, { nullable: true })
  dateTime: Date;

  @Field(() => Int, { nullable: true })
  client: number;
}
